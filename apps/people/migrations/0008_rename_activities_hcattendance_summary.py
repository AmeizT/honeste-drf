# Generated by Django 4.2.3 on 2023-07-22 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_homecell_members_testimony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hcattendance',
            old_name='activities',
            new_name='summary',
        ),
    ]
