from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=20)
    mobil = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients', blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '%s-%s_%s' % (self.first_name, self.last_name, self.company_name)


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts')
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE, related_name='contracts')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return '%s' % (self.id)


class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % (self.status)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(
        to=Contract, on_delete=models.CASCADE, related_name='events', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    event_status = models.ForeignKey(
        to=EventStatus, on_delete=models.CASCADE, default=1)
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
