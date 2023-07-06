# Generated by Django 4.2.1 on 2023-07-05 23:59

import apps.resources.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.resources.models.storageURL)),
                ('file', models.FileField(upload_to='uploads/', validators=[apps.resources.models.validate_non_image_file])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='file',
            name='dir',
        ),
        migrations.DeleteModel(
            name='Directory',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
