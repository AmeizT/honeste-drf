# Generated by Django 4.2.9 on 2024-02-04 11:07

import apps.office.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('churches', '0012_alter_church_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0017_alter_meeting_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('document_thumbnail_fallback', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Circular',
            fields=[
                ('abstractbasedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='office.abstractbasedocument')),
                ('uploaded_document', models.FileField(blank=True, null=True, upload_to=apps.office.utils.uploaded_circular_path)),
                ('category', models.CharField(blank=True, choices=[('strategy', 'Strategy'), ('president', 'President Circular'), ('general', 'General Overseer Circular'), ('national', 'National Overseer Circular'), ('secretary', 'Secretary General Circular')], max_length=255)),
            ],
            options={
                'verbose_name': 'Circular',
                'verbose_name_plural': 'Circulars',
                'ordering': ['-created_at'],
            },
            bases=('office.abstractbasedocument',),
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('abstractbasedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='office.abstractbasedocument')),
                ('uploaded_document', models.FileField(blank=True, null=True, upload_to=apps.office.utils.uploaded_strategy_path)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=255)),
                ('remarks', models.TextField(blank=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='churches.church')),
                ('moderated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='strategy_moderator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'strategy',
                'verbose_name_plural': 'strategies',
                'ordering': ['-created_at'],
            },
            bases=('office.abstractbasedocument',),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
