# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_column', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_column_column', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='multicolumns',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_column_multicolumns', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
