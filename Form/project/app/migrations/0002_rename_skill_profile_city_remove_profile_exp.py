# Generated by Django 5.1.2 on 2024-10-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='skill',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exp',
        ),
    ]
