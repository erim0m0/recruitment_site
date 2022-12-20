# Generated by Django 4.1 on 2022-12-18 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_educational_record_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='educational_record',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='language',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='work_experience',
        ),
        migrations.AddField(
            model_name='educationalrecord',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='educationalrecord',
            name='user',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='user',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
