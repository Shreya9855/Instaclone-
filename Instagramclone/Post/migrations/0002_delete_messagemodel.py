# Generated by Django 4.0.3 on 2022-03-25 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageModel',
        ),
    ]