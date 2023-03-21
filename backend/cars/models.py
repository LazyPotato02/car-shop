from django.db import models


# Create your models here.

class Cars(models.Model):
    make = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
    )
    engine_type = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
