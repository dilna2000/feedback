# Generated by Django 3.2.4 on 2022-03-12 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='happy',
        ),
    ]
