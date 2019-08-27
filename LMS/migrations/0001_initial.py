# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Book_ID')),
                ('Available', models.BooleanField(default=1)),
                ('Title', models.CharField(default='', max_length=64)),
                ('Author', models.CharField(default='', max_length=32)),
                ('ISBN', models.CharField(default='', max_length=32)),
                ('Publisher', models.CharField(default='', max_length=32)),
                ('Pub_Time', models.DateField(null=True)),
                ('Pages', models.IntegerField(null=True)),
                ('Description', models.TextField(null=True)),
                ('Position', models.CharField(default='A-101', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Reader_ID')),
                ('Name', models.CharField(max_length=16, unique=True)),
                ('Password', models.CharField(max_length=16)),
                ('Active', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('Modified_time', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Record_ID')),
                ('Created_time', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('WAITFORCHECK', 'WAITFORCHECK'), ('BORROWED', 'BORROWED'), ('RETURN', 'RETURNED'), ('TURNDOWN', 'TURNDOWN')], default='WAITFORCHECK', max_length=16)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='The_Book', to='LMS.Book')),
                ('Reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMS.Reader')),
            ],
        ),
    ]
