# Generated by Django 4.0.3 on 2022-06-08 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_action_option'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Action',
        ),
    ]