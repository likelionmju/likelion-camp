# Generated by Django 2.2.11 on 2020-07-01 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0005_auto_20200701_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='title',
        ),
    ]
