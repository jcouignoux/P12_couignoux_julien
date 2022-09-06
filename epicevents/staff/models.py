from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(AbstractUser):
    pass

    # class GroupName(models.TextChoices):
    #     MANAGEMENT = 'MA', _('Management')
    #     SALES = 'SA', _('Sales')
    #     SUPPORT = 'SU', _('Support')

    # groups = models.CharField(
    #     max_length=2,
    #     choices=GroupName.choices,
    # )

    # def is_in_group(self):
    #     return self.group


class CustomGroup(models.Model):

    group = models.OneToOneField(
        to=Group, unique=True, on_delete=models.DO_NOTHING)

    def name(self):
        class GroupName(models.TextChoices):
            MANAGEMENT = 'MA', _('Management')
            SALES = 'SA', _('Sales')
            SUPPORT = 'SU', _('Support')

        name = models.CharField(
            max_length=2,
            choices=GroupName.choices,
        )

        group_name = models.CharField(
            max_length=2,
            choices=GroupName.choices,
        )

        return group_name
