# Generated by Django 5.0.6 on 2024-06-04 07:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rate_limit', models.IntegerField()),
                ('burst_limit', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RateLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('limit_per_minute', models.IntegerField()),
                ('burst_limit', models.IntegerField()),
                ('last_checked', models.DateTimeField(auto_now=True)),
                ('tokens', models.FloatField(default=0)),
                ('merchant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rate_limiter_app.merchant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
