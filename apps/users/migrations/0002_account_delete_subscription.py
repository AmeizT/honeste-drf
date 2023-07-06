# Generated by Django 4.2.1 on 2023-07-06 00:04

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Free', 'Free'), ('Premium', 'Premium')], default='Free', max_length=255)),
                ('method', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Visa', 'Visa'), ('Mastercard', 'Mastercard')], max_length=255)),
                ('intervals', models.IntegerField(choices=[(1, 'Monthly'), (4, 'Quarterly'), (12, 'Annually')], default=0)),
                ('premium_fee', models.DecimalField(decimal_places=2, default=Decimal('5'), max_digits=10)),
                ('sub_total', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('amount_due', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
                'ordering': ['-created'],
            },
        ),
    ]
