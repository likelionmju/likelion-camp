# Generated by Django 3.0.5 on 2020-07-27 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hw', '0003_homework_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]