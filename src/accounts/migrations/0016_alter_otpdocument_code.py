# Generated by Django 4.1 on 2022-08-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_otpdocument_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpdocument',
            name='code',
            field=models.PositiveIntegerField(verbose_name='Otp Code'),
        ),
    ]