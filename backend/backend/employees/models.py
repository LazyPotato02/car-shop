
from django.core import validators
from django.db import models

from backend.base.validators import validate_only_letters
from backend.cells.models import Cells


# Create your models here.


class Employee(models.Model):
    class Meta:
        ordering = ('first_name',)

    first_name = models.CharField(
        max_length=40,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(2),
        ),
        verbose_name='First Name',
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=40,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(2),
        ),
        verbose_name='Last Name',
        blank=False,
        null=False,
    )

    cell = models.ManyToManyField(Cells)
    emp_id = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Employee Id'
    )

