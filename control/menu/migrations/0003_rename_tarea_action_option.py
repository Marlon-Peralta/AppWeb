# Generated by Django 4.0.3 on 2022-06-07 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_tarea_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='tarea',
            new_name='option',
        ),
    ]