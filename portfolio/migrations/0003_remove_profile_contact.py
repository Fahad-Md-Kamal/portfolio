# Generated by Django 3.2.8 on 2021-10-21 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
    ]