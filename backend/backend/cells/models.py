from django.db import models

# Create your models here.
class Cells(models.Model):
    cell_name = models.CharField(max_length=25, unique=True)