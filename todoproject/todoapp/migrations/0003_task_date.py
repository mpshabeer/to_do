# Generated by Django 3.2.20 on 2023-08-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_name_task_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-01-17'),
            preserve_default=False,
        ),
    ]
