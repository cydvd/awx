# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 21:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_v330_move_deprecated_stdout'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSessionMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sessions.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]