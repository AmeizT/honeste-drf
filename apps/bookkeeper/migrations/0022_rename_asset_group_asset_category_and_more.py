# Generated by Django 5.0.1 on 2024-01-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0021_alter_asset_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='asset_group',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='editor',
            new_name='created_by',
        ),
        migrations.AddField(
            model_name='asset',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
