# Generated by Django 2.0.1 on 2018-06-28 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0030_auto_20180628_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='publication',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='materials.Publication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='num_authors',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]