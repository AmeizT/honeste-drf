# Generated by Django 4.2.9 on 2024-05-10 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookkeeper', '0029_rename_expense_type_expenditure_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenditure_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
