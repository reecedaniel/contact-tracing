# Generated by Django 3.0.3 on 2020-06-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0006_auto_20200623_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
