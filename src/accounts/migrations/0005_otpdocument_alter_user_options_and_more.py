# Generated by Django 4.1 on 2022-08-17 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(6)], verbose_name='Otp Code')),
                ('contact', models.CharField(max_length=12, verbose_name='Contact')),
                ('expire_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Otp Service',
                'verbose_name_plural': 'Otp Services',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-id',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number.', regex='^989\\d{2}\\s*?\\d{3}\\s*?\\d{4}$')], verbose_name='phone'),
        ),
    ]