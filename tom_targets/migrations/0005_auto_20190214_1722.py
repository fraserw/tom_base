# Generated by Django 2.1.5 on 2019-02-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0004_auto_20190123_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetextra',
            name='bool_value',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='targetextra',
            name='float_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='targetextra',
            name='time_value',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
