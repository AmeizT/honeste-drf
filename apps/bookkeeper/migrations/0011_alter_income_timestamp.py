# Generated by Django 4.2.3 on 2023-12-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0010_alter_income_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
