# Generated by Django 4.1 on 2022-09-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(choices=[('normal', 'کاربر عادی'), ('admin', 'ادمین'), ('superuser', 'ابر یوزر')], default='normal', max_length=9, verbose_name='User Level'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
