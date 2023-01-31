from django.db import models


# Create your models here.
class Cells(models.Model):
    cell_name = models.CharField(max_length=3, unique=True)

    class Meta:
        ordering = ('cell_name',)

    def __str__(self):
        return self.cell_name
