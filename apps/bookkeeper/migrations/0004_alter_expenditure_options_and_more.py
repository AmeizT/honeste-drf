# Generated by Django 4.2.3 on 2023-09-29 16:24

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeper', '0003_alter_expenditure_receipt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenditure',
            options={'ordering': ['-created_at'], 'verbose_name': 'Expenditure', 'verbose_name_plural': 'Expenditure'},
        ),
        migrations.RenameField(
            model_name='expenditure',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='expenditure',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='funds_received',
            new_name='remittance',
        ),
        migrations.RemoveField(
            model_name='income',
            name='bank_statement',
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='receipt',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.CreateModel(
            name='BankStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('attachment', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('income_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_entry', to='bookkeeper.income')),
            ],
            options={
                'verbose_name': 'Bank Statement',
                'verbose_name_plural': 'Bank Statements',
                'ordering': ['-created_at'],
            },
        ),
    ]
