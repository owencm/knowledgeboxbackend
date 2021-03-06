from django.http import HttpResponse
from django.utils import simplejson
import datetime
from django.utils.timezone import utc
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from backend.models import QaItem, User

def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = simplejson.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator

def serialiseItem(qaitem):
	return {"question": qaitem.question, "answer": qaitem.answer, "id": qaitem.id, "url": qaitem.url}

@csrf_exempt
def qaitem_index(request):
	if request.method == 'GET':

		qaitems = QaItem.objects.all()
		qaitems_serialised = map(serialiseItem, qaitems)
		output_json = simplejson.dumps(qaitems_serialised)
		return HttpResponse(output_json, mimetype='application/json')

	elif request.method == 'POST':
		data = request.POST
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		qaitem = QaItem(question=data.get("question"), answer=data.get("answer"), url=data.get("url"), creator_id=1, created_at=now)
		qaitem.save()

		user = User.objects.get(id=data.get("user_id"))
		user.qaitem_set.add(qaitem)

		qaitem_serialised = serialiseItem(qaitem)
		output_json = simplejson.dumps(qaitem_serialised)
		return HttpResponse(output_json, mimetype='application/json') 

def qaitem(request, qaitem_id):
	qaitem = serialiseItem(QaItem.objects.filter(id=qaitem_id)[0])
	output_json = simplejson.dumps(qaitem)
	return HttpResponse(output_json, mimetype='application/json') 

def qaitem_index_filter_by_url(request, url):
	qaitems = QaItem.objects.filter(url=url)
	qaitems_serialised = map(serialiseItem, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

def qaitem_index_filter_by_url_including_learning(request, user_id, url):
	qaitems = QaItem.objects.filter(url=url)
	user = User.objects.get(id=user_id)
	qaitems_serialised = map(lambda qaitem: {"question": qaitem.question, "answer": qaitem.answer, "id": qaitem.id, "url": qaitem.url, "learning": user in qaitem.learners.all()}, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

@json_response
def qaitem_index_filter_by_learning(request, user_id):
	user = User.objects.get(id=user_id)
	qaitems = user.qaitem_set.all()
	qaitems_serialised = map(serialiseItem, qaitems)
	return qaitems_serialised

@csrf_exempt
def qaitem_learn(request, qaitem_id):
	qaitem = QaItem.objects.get(id=qaitem_id)
	data = request.POST
	user = User.objects.get(id=data.get("user_id"))
	qaitem.learners.add(user)
	return HttpResponse(simplejson.dumps({"success": True})) 

@csrf_exempt
def qaitem_forget(request, qaitem_id):
	qaitem = QaItem.objects.get(id=qaitem_id)
	data = request.POST
	user = User.objects.get(id=data.get("user_id"))
	qaitem.learners.remove(user)
	return HttpResponse(simplejson.dumps({"success": True})) 

@csrf_exempt
def login(request):
	data = request.POST
	user = User.objects.get(username=data.get("username"))
	if data.get("password") == user.password:
		response = {"success": True, "id": str(user.id)}
		return HttpResponse(simplejson.dumps(response))
	else:
		response = {"success": False}
		return HttpResponse(simplejson.dumps(response))
	
@csrf_exempt
def register(request):
	data = request.POST
	existing_user = User.objects.filter(username=data.get("username"))
	if existing_user.count() == 0:
		user = User(username=data.get("username"), password=data.get("password"))
		user.save()
		user_serialised = {"username": user.username, "password": user.password, "id": user.id}
		output_json = simplejson.dumps(user_serialised)
	else:
		output_json = simplejson.dumps({"success": False})
	return HttpResponse(output_json, mimetype='application/json')

@csrf_exempt
def qresponse(request):
	data = request.POST
	n = datetime.datetime.utcnow().replace(tzinfo=utc)
	qresp = QResponse(qid=data.get("qid"), userid=data.get("user_id"), correct=data.get("correct"), time=n)
	qresp.save()
	qresp_serialised = {"id": qresp.id, "qid": qresp.qid, "user_id":qresp.userid, "correct": qresp.correct, "time":qresp.time}
	output_json = simplejson.dumps(qresp_serialised)
	return HttpResponse(output_json, mimetype='application/json')

# # Create your views here.

# from django.http import HttpResponse
# from django.utils import simplejson

# from backend.models import QaItem

# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.response import Response
# from backend.serializers import QaItemSerializer

# class QaItemList(generics.ListCreateAPIView):
# 	"""
# 	API endpoint that represents a list of qaitems.
# 	"""
# 	model = QaItem
# 	serializer_class = QaItemSerializer

# class QaItemDetail(generics.RetrieveUpdateDestroyAPIView):
# 	model = QaItem
# 	serializer_class = QaItemSerializer