from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'creator']
