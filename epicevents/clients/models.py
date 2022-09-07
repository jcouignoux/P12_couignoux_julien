from django.conf import settings
from django.db import models
from django.db.models import Q


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
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients', blank=True, null=True, limit_choices_to=Q(groups__name='Sales'))
    status = models.BooleanField(default=False)

    def __str__(self):
        return '%s-%s_%s' % (self.first_name, self.last_name, self.company_name)
