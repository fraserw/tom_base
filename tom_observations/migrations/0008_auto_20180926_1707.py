# Generated by Django 2.1.1 on 2018-09-26 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tom_observations', '0007_auto_20180924_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataproductgroup',
            options={'ordering': ('-created',)},
        ),
    ]