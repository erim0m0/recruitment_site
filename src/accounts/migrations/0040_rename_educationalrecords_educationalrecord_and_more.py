# Generated by Django 4.1 on 2022-09-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_remove_profile_about_person_remove_profile_cv_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EducationalRecords',
            new_name='EducationalRecord',
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='about_me',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='About Me'),
        ),
    ]