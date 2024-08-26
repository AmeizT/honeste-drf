# Generated by Django 4.2.9 on 2024-08-25 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0032_rename_church_asset_assembly_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='image',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='assetimage',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_images', to='bookkeeper.asset'),
        ),
    ]
