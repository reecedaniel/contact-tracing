# Generated by Django 3.0.3 on 2020-06-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0009_auto_20200623_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
