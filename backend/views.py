# Create your views here.

from django.http import HttpResponse
from django.utils import simplejson

from backend.models import QaItem

def qaitem_index(request):
	qaitems = QaItem.objects.all()
	qaitems_serialised = map(lambda qaitem: {"question": qaitem.question, "answer": qaitem.answer} , qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

def qaitem(request, qaitem_id):
	return HttpResponse("Hello, world. You're viewing qaitem %s." % qaitem_id) 