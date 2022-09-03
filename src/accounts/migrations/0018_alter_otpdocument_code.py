# Generated by Django 4.1 on 2022-08-17 17:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_otpdocument_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpdocument',
            name='code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)], verbose_name='Otp Code'),
        ),
    ]