# Generated by Django 4.1 on 2022-09-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_blockedphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpdocument',
            name='code',
            field=models.PositiveIntegerField(verbose_name='Otp Code'),
        ),
    ]
