# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtomicPositions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=20)),
                ('codeversion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=300)),
                ('pub_title', models.CharField(max_length=100)),
                ('pub_vol', models.CharField(max_length=100)),
                ('pub_pages_start', models.CharField(max_length=10)),
                ('pub_pages_end', models.CharField(max_length=10)),
                ('pub_date', models.CharField(max_length=4)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('doi_isbn', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_name', models.CharField(max_length=100)),
                ('aminoacid', models.CharField(max_length=100)),
                ('shortname', models.CharField(max_length=4)),
                ('organic', models.TextField(max_length=30)),
                ('inorganic', models.TextField(max_length=10)),
                ('formula', models.CharField(max_length=100)),
                ('charge', models.FloatField()),
                ('last_update', models.DateField()),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.AddField(
            model_name='atomicpositions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.Author'),
        ),
        migrations.AddField(
            model_name='atomicpositions',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.Contributor'),
        ),
        migrations.AddField(
            model_name='atomicpositions',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.System'),
        ),
    ]
