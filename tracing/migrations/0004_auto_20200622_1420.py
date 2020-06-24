# Generated by Django 3.0.3 on 2020-06-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0003_auto_20200622_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='breathing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='dry_cough',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='flu',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visit',
            name='other_contact',
            field=models.BooleanField(default=False),
        ),
    ]
