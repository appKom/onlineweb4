# Generated by Django 2.1.9 on 2019-08-23 14:20

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0007_auto_20190506_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images_csv',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]