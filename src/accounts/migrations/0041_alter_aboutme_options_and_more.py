# Generated by Django 4.1 on 2022-09-22 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_rename_educationalrecords_educationalrecord_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About Me', 'verbose_name_plural': 'About Me'},
        ),
        migrations.AlterModelOptions(
            name='educationalrecord',
            options={'verbose_name': 'Educational Record', 'verbose_name_plural': 'Educational Records'},
        ),
        migrations.AlterModelOptions(
            name='personalinformation',
            options={'verbose_name': 'Personal Information', 'verbose_name_plural': 'Personal Informations'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'verbose_name': 'Work Experience', 'verbose_name_plural': 'Work Experiences'},
        ),
        migrations.AddField(
            model_name='aboutme',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='educationalrecord',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='educationalrecord',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
