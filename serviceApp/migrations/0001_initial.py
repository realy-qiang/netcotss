# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-21 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountApp', '0001_initial'),
        ('TariffApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('unix_host', models.CharField(max_length=32)),
                ('os_username', models.CharField(max_length=64)),
                ('login_passwd', models.CharField(max_length=32)),
                ('status', models.NullBooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('pause_date', models.DateTimeField(null=True)),
                ('close_date', models.DateTimeField(null=True)),
                ('s_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountApp.Account')),
                ('s_usercost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TariffApp.UserCost')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
