# Generated by Django 4.1 on 2022-12-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_alter_advertisement_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='language',
            field=models.CharField(max_length=100, verbose_name='Languages'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='salary',
            field=models.CharField(db_index=True, max_length=75, verbose_name='Salary'),
        ),
    ]
