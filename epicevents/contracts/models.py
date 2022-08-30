from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

from clients.models import Client

# Create your models here.


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts', limit_choices_to=Q(groups__name='Sales'))
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE, related_name='contracts')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return '%s' % (self.id)
