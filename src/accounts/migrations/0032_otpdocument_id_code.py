# Generated by Django 4.1 on 2022-09-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_otpdocument_contact_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpdocument',
            name='id_code',
            field=models.CharField(default=11, editable=False, max_length=32, verbose_name='ID Code'),
            preserve_default=False,
        ),
    ]