# Create your views here.

from django.http import HttpResponse
from django.utils import simplejson

from backend.models import QaItem

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from backend.serializers import QaItemSerializer

class QaItemList(generics.ListCreateAPIView):
	"""
	API endpoint that represents a list of qaitems.
	"""
	model = QaItem
	serializer_class = QaItemSerializer

class QaItemDetail(generics.RetrieveUpdateDestroyAPIView):
	model = QaItem
	serializer_class = QaItemSerializer