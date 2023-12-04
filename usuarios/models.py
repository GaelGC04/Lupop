from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, null=False)
    phone_number = models.CharField(_('phone number'), max_length=15, unique=True, null=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'phone_number']