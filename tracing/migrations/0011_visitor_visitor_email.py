# Generated by Django 3.0.3 on 2020-06-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracing', '0010_auto_20200624_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='visitor_email',
            field=models.EmailField(default='example@example.com', max_length=254),
            preserve_default=False,
        ),
    ]
