# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='expected_learnings',
            field=models.TextField(verbose_name="What you'll learn", default=None, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='full_description',
            field=models.TextField(verbose_name='About this course', default=None, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='level_type',
            field=models.ForeignKey(null=True, to='course_metadata.LevelType', default=None, blank=True, related_name='publisher_courses', verbose_name='Course level'),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(verbose_name='Course number', blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='organizations',
            field=models.ManyToManyField(to='course_metadata.Organization', related_name='publisher_courses', blank=True, verbose_name='Partner Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(verbose_name='Course subtitle', default=None, blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(verbose_name='Course title', default=None, blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='expected_learnings',
            field=models.TextField(verbose_name="What you'll learn", default=None, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='full_description',
            field=models.TextField(verbose_name='About this course', default=None, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='number',
            field=models.CharField(verbose_name='Course number', blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='short_description',
            field=models.CharField(verbose_name='Course subtitle', default=None, blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='title',
            field=models.CharField(verbose_name='Course title', default=None, blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historicalseat',
            name='type',
            field=models.CharField(choices=[('honor', 'Honor'), ('audit', 'Audit'), ('verified', 'Verified'), ('professional', 'Professional (with ID verification)'), ('no-id-professional', 'Professional (no ID verifiation)'), ('credit', 'Credit')], max_length=63, verbose_name='Course type'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='currency',
            field=models.ForeignKey(related_name='publisher_seats', to='core.Currency', default='USD'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='type',
            field=models.CharField(choices=[('honor', 'Honor'), ('audit', 'Audit'), ('verified', 'Verified'), ('professional', 'Professional (with ID verification)'), ('no-id-professional', 'Professional (no ID verifiation)'), ('credit', 'Credit')], max_length=63, verbose_name='Course type'),
        ),
    ]
