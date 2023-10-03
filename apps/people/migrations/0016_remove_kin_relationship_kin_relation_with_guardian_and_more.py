# Generated by Django 4.2.3 on 2023-10-03 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0015_alter_member_created_by_kin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kin',
            name='relationship',
        ),
        migrations.AddField(
            model_name='kin',
            name='relation_with_guardian',
            field=models.CharField(blank=True, choices=[('Aunt', 'Aunt'), ('Brother', 'Brother'), ('Child', 'Child'), ('Cousin', 'Cousin'), ('Grandparent', 'Grandparent'), ('Sister', 'Sister'), ('Spouse', 'Spouse'), ('Uncle', 'Uncle')], max_length=255),
        ),
        migrations.AlterField(
            model_name='kin',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kin_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
