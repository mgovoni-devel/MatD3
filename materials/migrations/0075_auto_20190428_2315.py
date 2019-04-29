# Generated by Django 2.1.7 on 2019-04-29 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0074_auto_20190422_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={},
        ),
        migrations.AlterField(
            model_name='dataset',
            name='primary_property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='primary_property', to='materials.Property'),
            preserve_default=False,
        ),
    ]
