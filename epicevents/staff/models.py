from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):

    class Group(models.TextChoices):
        MANAGEMENT = 'MA', _('Management')
        SALES = 'SA', _('Sales')
        SUPPORT = 'SU', _('Support')

        # group = models.CharField(
        #     max_length=2,
        #     choices=Group,
        # )

    # def is_in_group(self):
    #     return self.group
