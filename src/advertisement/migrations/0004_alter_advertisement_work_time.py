# Generated by Django 4.1 on 2023-01-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_alter_advertisement_maximum_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='work_time',
            field=models.TimeField(blank=True, max_length=250, null=True, verbose_name='work time'),
        ),
    ]
