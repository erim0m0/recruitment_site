# Generated by Django 4.1 on 2022-09-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_personalinformation_profile_avatar_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]