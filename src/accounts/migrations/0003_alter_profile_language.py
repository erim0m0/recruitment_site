# Generated by Django 4.1 on 2023-01-08 09:00

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_companyprofile_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Persian', 'Persian'), ('English', 'English')], max_length=30, verbose_name='language'),
        ),
    ]
