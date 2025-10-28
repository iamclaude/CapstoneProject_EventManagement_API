from django.db import models
from django.conf import settings
from events.models import Event

class Ticket(models.Model):
    TICKET_TYPES = [
        ('REGULAR', 'Regular'),
        ('VIP', 'VIP'),
        ('EARLY_BIRD', 'Early Bird'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        related_name="tickets"
    )
    ticket_type = models.CharField(
        max_length=20, 
        choices=TICKET_TYPES, 
        default='REGULAR'
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.ticket_type})"
