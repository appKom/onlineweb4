# Generated by Django 3.0.5 on 2020-05-19 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification", old_name="from_mail", new_name="from_email",
        ),
    ]