from backend.models import QaItem
from rest_framework import serializers

class QaItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QaItem
        fields = ('question', 'answer')