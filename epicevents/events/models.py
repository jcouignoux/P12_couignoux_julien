from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from contracts.models import Contract

# Create your models here.


class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.status)

    class Meta:
        verbose_name_plural = "Event Status"


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(
        to=Contract, on_delete=models.CASCADE, related_name='events', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', limit_choices_to=Q(groups__name='Support'))
    event_status = models.ForeignKey(
        to=EventStatus, on_delete=models.CASCADE, default=1)
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
