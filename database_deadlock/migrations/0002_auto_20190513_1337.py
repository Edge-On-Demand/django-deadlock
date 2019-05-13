# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-13 17:37
from __future__ import unicode_literals
import os

from django.db import migrations
from django.db import connection


PROJECT_DIR = os.path.dirname(__file__)


def install_sql(apps, schema_editor):
    connection.cursor().execute(open(os.path.join(PROJECT_DIR, '../sql/deadlock.sqlite3.sql')).read())
    

class Migration(migrations.Migration):

    dependencies = [
        ('database_deadlock', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(install_sql, reverse_code=migrations.RunPython.noop),
    ]