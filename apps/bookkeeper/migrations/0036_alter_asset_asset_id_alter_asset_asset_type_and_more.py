# Generated by Django 4.2.9 on 2024-08-25 23:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0035_alter_asset_asset_type_alter_asset_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.UUIDField(default=uuid.UUID, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('Building', 'Building'), ('Instrument', 'Instrument'), ('Vehicle', 'Vehicle'), ('Furniture', 'Furniture'), ('Electronics', 'Electronics'), ('Machinery', 'Machinery'), ('Software', 'Software'), ('Land', 'Land'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Good', 'Good'), ('Fair', 'Fair'), ('Old', 'Old'), ('Not Working', 'Not Working')], max_length=20),
        ),
    ]
