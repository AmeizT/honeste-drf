# Generated by Django 4.2.9 on 2024-04-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0026_alter_attendance_options_alter_homecell_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homecell',
            name='non_church_members',
            field=models.TextField(blank=True),
        ),
    ]
