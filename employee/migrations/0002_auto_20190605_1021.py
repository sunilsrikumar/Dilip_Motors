# Generated by Django 2.2.2 on 2019-06-05 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_detail',
            name='joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]