# Generated by Django 3.0.5 on 2020-05-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stacklion', '0005_question_question_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
