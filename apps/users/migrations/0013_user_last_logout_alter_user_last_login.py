# Generated by Django 4.2.9 on 2024-05-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
