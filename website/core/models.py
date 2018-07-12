from django.db import models
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    """
    Abstract base model from which other models will inherit from.
    """
    created = models.DateTimeField(
        auto_now_add=True,
        null=True, blank=True,
        help_text='Record first created date and time'
    )
    modified = models.DateTimeField(
        auto_now=True,
        null=True, blank=True,
        help_text='Record last modified date and time'
    )

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    pass
