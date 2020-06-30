# Generated by Django 3.0.3 on 2020-06-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('cellphone', models.CharField(max_length=10, unique=True)),
                ('visitor_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('dry_cough', models.BooleanField(default=False)),
                ('breathing', models.BooleanField(default=False)),
                ('flu', models.BooleanField(default=False)),
                ('other_contact', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cellphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracing.Visitor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
            ],
        ),
    ]
