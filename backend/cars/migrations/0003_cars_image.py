# Generated by Django 4.1.7 on 2023-03-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.CharField(default=None, max_length=9999),
            preserve_default=False,
        ),
    ]