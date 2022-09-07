from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):

    class Name(models.TextChoices):
        MANAGEMENT = 'MA', _('Management')
        SALES = 'SA', _('Sales')
        SUPPORT = 'SU', _('Support')

    role = models.CharField(
        max_length=2,
        choices=Name.choices,
        default=None,
        blank=True,
        null=True
    )
