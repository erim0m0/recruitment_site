# Generated by Django 4.1 on 2022-11-03 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_companyprofile_organizational_interface'),
        ('advertisement', '0004_alter_advertisement_benefits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='company',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='accounts.companyprofile'),
        ),
    ]