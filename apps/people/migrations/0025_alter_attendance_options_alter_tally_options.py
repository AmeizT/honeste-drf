# Generated by Django 4.2.9 on 2024-03-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0024_rename_editor_attendance_created_by_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['attendance_date'], 'verbose_name': 'attendance', 'verbose_name_plural': 'attendance'},
        ),
        migrations.AlterModelOptions(
            name='tally',
            options={'ordering': ['timestamp'], 'verbose_name': 'tally', 'verbose_name_plural': 'tallies'},
        ),
    ]
