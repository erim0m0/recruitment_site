# Generated by Django 4.1 on 2022-11-06 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import extensions.utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_companyprofile_organizational_interface'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=10, null=True, verbose_name='Slug Field')),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='educationalrecord',
            name='grade',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Birth'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'F'), ('Male', 'M')], max_length=6, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_married',
            field=models.BooleanField(default=False, verbose_name='Is Married ?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='military_service_status',
            field=models.CharField(blank=True, choices=[('end of service', 'the end of service'), ('permanent exemption', 'permanent exemption'), ('education pardon', 'education pardon'), ('doing', 'doing'), ('included', 'included')], max_length=100, null=True, verbose_name='Military Service Status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[extensions.utils.email_validator], verbose_name='Email'),
        ),
        migrations.DeleteModel(
            name='PersonalInformation',
        ),
    ]