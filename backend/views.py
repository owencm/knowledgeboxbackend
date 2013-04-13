# Create your views here.

from django.http import HttpResponse
from django.utils import simplejson

from backend.models import QaItem

def serialiseItem(qaitem):
	return {"question": qaitem.question, "answer": qaitem.answer}

def qaitem_index(request):
	qaitems = QaItem.objects.all()
	qaitems_serialised = map(serialiseItem, qaitems)
	output_json = simplejson.dumps(qaitems_serialised)
	return HttpResponse(output_json, mimetype='application/json')

def qaitem(request, qaitem_id):
	qaitem = serialiseItem(QaItem.objects.filter(id=qaitem_id)[0])
	output_json = simplejson.dumps(qaitem)
	return HttpResponse(output_json, mimetype='application/json') 