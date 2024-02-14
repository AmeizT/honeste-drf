# Generated by Django 4.2.9 on 2024-02-04 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0012_alter_church_status'),
        ('office', '0018_abstractbasedocument_circular_strategy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='branch',
        ),
        migrations.AddField(
            model_name='strategy',
            name='assembly',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='assembly_strategy', to='churches.church'),
            preserve_default=False,
        ),
    ]
