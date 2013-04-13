from django.http import HttpResponse
from django.utils import simplejson

from backend.models import QaItem

def serialiseItem(qaitem):
	return {"question": qaitem.question, "answer": qaitem.answer, "id": qaitem.id}

def qaitem_index(request):
	qaitems = QaItem.objects.all()
	qaitems_serialised = map(serialiseItem, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

def qaitem(request, qaitem_id):
	qaitem = serialiseItem(QaItem.objects.filter(id=qaitem_id)[0])
	output_json = simplejson.dumps(qaitem)
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