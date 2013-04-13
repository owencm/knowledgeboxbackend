from django.http import HttpResponse
from django.utils import simplejson
import datetime
from django.utils.timezone import utc
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from backend.models import QaItem

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
		qaitem = QaItem(question=data.get("question"), answer=data.get("answer"), creator_id=1, created_at=now)
		qaitem.save()
		return HttpResponse("")

def qaitem(request, qaitem_id):
	qaitem = serialiseItem(QaItem.objects.filter(id=qaitem_id)[0])
	output_json = simplejson.dumps(qaitem)
	return HttpResponse(output_json, mimetype='application/json') 

def qaitem_index_filter_by_url(request, url):
	qaitems = QaItem.objects.filter(url=url)
	qaitems_serialised = map(serialiseItem, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
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