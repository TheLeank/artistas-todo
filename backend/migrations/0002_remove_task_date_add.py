# Generated by Django 3.1 on 2020-11-21 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_add',
        ),
    ]
