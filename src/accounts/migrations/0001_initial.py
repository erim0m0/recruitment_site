# Generated by Django 4.1 on 2023-03-05 15:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import extensions.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone', models.CharField(max_length=10, unique=True, validators=[extensions.utils.phone_validator], verbose_name='phone')),
                ('user_level', models.CharField(choices=[('normal', 'normal'), ('admin', 'admin'), ('super_user', 'super_user')], default='normal', max_length=10, verbose_name='user level')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active_email', models.BooleanField(default=False)),
                ('is_operator', models.BooleanField(default=False)),
                ('active_email_code', models.CharField(editable=False, max_length=32)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='BlockedPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='شماره ی تلفن نامعتبر است.', regex='^9\\d{2}\\s*?\\d{3}\\s*?\\d{4}$')], verbose_name='phone')),
            ],
            options={
                'verbose_name': 'Blocked Phone',
                'verbose_name_plural': 'Blocked Phones',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Industry',
                'verbose_name_plural': 'Industries',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=254, validators=[extensions.utils.email_validator], verbose_name='Email')),
                ('avatar', models.ImageField(blank=True, upload_to='profiles/avatars/', verbose_name='Avatar')),
                ('national_code', models.CharField(max_length=10, unique=True, validators=[extensions.utils.national_code_validator], verbose_name='National code')),
                ('passport_number', models.CharField(blank=True, max_length=20, verbose_name='Passport number')),
                ('country', models.CharField(default='ایران', max_length=20, verbose_name='Country')),
                ('province', models.CharField(max_length=100, verbose_name='Province')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('address', models.TextField(blank=True, max_length=300, verbose_name='Address')),
                ('is_married', models.BooleanField(default=False, verbose_name='Is Married ?')),
                ('gender', models.CharField(choices=[('female', 'خانم'), ('male', 'آقا')], max_length=6, verbose_name='Gender')),
                ('date_of_birth', models.DateField(verbose_name='Date Of Birth')),
                ('military_service_status', models.CharField(choices=[('دارای کارت پایان خدمت', 'دارای کارت پایان خدمت'), ('در حال خدمت', 'در حال خدمت'), ('معاف از رزم', 'معاف از رزم'), ('معافیت تحصیلی', 'معافیت تحصیلی'), ('معافیت پزشکی', 'معافیت پزشکی'), ('سایر معافیت ها', 'سایر معافیت ها')], max_length=100, verbose_name='Military Service Status')),
                ('other_exemptions', models.CharField(blank=True, max_length=100, verbose_name='Other Exemptions')),
                ('about_me', models.TextField(blank=True, max_length=300, verbose_name='About Me')),
                ('cv_file', models.ImageField(blank=True, upload_to='profiles/resumes/', verbose_name='CV File')),
                ('language', models.ManyToManyField(blank=True, to='accounts.language', verbose_name='Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('name', models.CharField(db_index=True, max_length=120, unique=True, verbose_name='name')),
                ('english_name', models.CharField(max_length=120, primary_key=True, serialize=False, verbose_name='english name')),
                ('email', models.EmailField(max_length=254, validators=[extensions.utils.email_validator], verbose_name='email')),
                ('website_addr', models.CharField(blank=True, max_length=100, unique=True, verbose_name='website address')),
                ('telephone', models.CharField(max_length=10, unique=True)),
                ('country', models.CharField(default='IR', max_length=2, verbose_name='country')),
                ('province', models.CharField(max_length=105, verbose_name='province')),
                ('city', models.CharField(max_length=105, verbose_name='city')),
                ('logo', models.ImageField(blank=True, upload_to='companies/logos/', verbose_name='logo')),
                ('company_description', models.TextField(blank=True, max_length=400, verbose_name='company description')),
                ('company_view', models.ImageField(blank=True, upload_to='companies/views/', verbose_name='company view')),
                ('established_year', models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='The year is Invalid.', regex='^1[34]\\d{2}$')], verbose_name='established year')),
                ('type_of_ownership', models.CharField(choices=[('private', 'خصوصی'), ('Governmental', 'دولتی'), ('other', 'غیره ( وقفی و ...)')], max_length=12, verbose_name='type of ownership')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('number_of_ad', models.PositiveIntegerField(default=0, verbose_name='number of advertisements')),
                ('industry', models.ManyToManyField(blank=True, to='accounts.industry', verbose_name='industry')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='operator')),
            ],
            options={
                'verbose_name': 'Company Profile',
                'verbose_name_plural': 'Companies Profile',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50, verbose_name='Job')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Work Experience',
                'verbose_name_plural': 'Work Experiences',
                'unique_together': {('user', 'job')},
            },
        ),
        migrations.CreateModel(
            name='EducationalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_study', models.CharField(max_length=30, verbose_name='field of study')),
                ('education', models.CharField(choices=[('DIPLOMA', 'Diploma'), ('ASSOCIATE', 'Associate'), ('BACHELOR', 'Bachelor'), ('MASTER', 'Master'), ('PHD', 'Phd'), ('POSTDOC', 'Postdoc')], max_length=9, verbose_name='education')),
                ('university', models.CharField(max_length=50, verbose_name='University')),
                ('score', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='score')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Educational Record',
                'verbose_name_plural': 'Educational Records',
                'unique_together': {('user', 'education')},
            },
        ),
    ]
