# Generated by Django 4.2.3 on 2023-12-03 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='post',
            new_name='discussion',
        ),
    ]
