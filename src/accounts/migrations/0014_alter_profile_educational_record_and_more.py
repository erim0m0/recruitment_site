# Generated by Django 4.1 on 2022-12-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_profile_work_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='educational_record',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_experience',
            field=models.JSONField(default=dict),
        ),
    ]
