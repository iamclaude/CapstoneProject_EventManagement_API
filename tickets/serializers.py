from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event_title = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Ticket
        fields = ['id', 'user', 'event', 'event_title', 'ticket_type', 'price', 'purchased_at']
