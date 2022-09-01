from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Create your models here.


class EventStatus(models.Model):

    class Status(models.TextChoices):
        OPEN = 'OP', _('Open')
        INPROGRESS = 'IP', _('In Progress')
        CLOSED = 'CL', _('Closed')

    id = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.OPEN)

    def __str__(self):
        return '%s' % (self.status)

    class Meta:
        verbose_name_plural = "Event Status"


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', limit_choices_to=Q(groups__name='Support'))
    event_status = models.ForeignKey(
        to=EventStatus, on_delete=models.CASCADE, default=1)
    attendees = models.PositiveIntegerField()
    event_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return '%s' % (self.id)
