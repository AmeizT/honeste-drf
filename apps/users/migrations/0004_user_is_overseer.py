# Generated by Django 4.2.1 on 2023-06-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_church'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_overseer',
            field=models.BooleanField(default=False),
        ),
    ]
