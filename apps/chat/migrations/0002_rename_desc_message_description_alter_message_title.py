# Generated by Django 4.2.9 on 2024-03-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
