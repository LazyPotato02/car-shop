from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Contact(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    text = models.TextField(
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email