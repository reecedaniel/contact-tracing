# Generated by Django 3.0.3 on 2020-07-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_max_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
