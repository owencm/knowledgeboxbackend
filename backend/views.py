from django.http import HttpResponse
from django.utils import simplejson
import datetime
from django.utils.timezone import utc
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from backend.models import QaItem, User

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

def qaitem_index_filter_by_learning(request, user_id):
	user = User.objects.get(id=user_id)
	qaitems = user.qaitem_set.all()
	qaitems_serialised = map(serialiseItem, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

@csrf_exempt
def qaitem_learn(request, qaitem_id):
	qaitem = QaItem.objects.get(id=qaitem_id)
	data = request.POST
	user = User.objects.get(id=data.get("user_id"))
	qaitem.learners.add(user)
	return HttpResponse("{success: true}") 

@csrf_exempt
def qaitem_forget(request, qaitem_id):
	qaitem = QaItem.objects.get(id=qaitem_id)
	data = request.POST
	user = User.objects.get(id=data.get("user_id"))
	qaitem.learners.remove(user)
	return HttpResponse("{success: true}") 

@csrf_exempt
def login(request):
	data = request.POST
	user = User.objects.get(username=data.get("username"))
	if data.get("password") == user.password:
		return HttpResponse("{success: true, id: " + user.id + " }")
	else:
		return HttpResponse("{success: false}")
	
@csrf_exempt
def register(request):
	data = request.POST
	user = User(username=data.get("username"), password=data.get("password"))
	user.save()
	user_serialised = {"username": user.username, "password": user.password, "id": user.id}
	output_json = simplejson.dumps(user_serialised)
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