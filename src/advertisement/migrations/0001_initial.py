# Generated by Django 4.1 on 2022-12-12 18:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='title')),
                ('organizational_category', models.CharField(max_length=75, verbose_name='organizational category')),
                ('type_of_cooperation', models.CharField(choices=[('full-time', 'full-time'), ('per time', 'per time'), ('remote', 'remote')], max_length=75, verbose_name='type of cooperation')),
                ('work_time', models.TimeField(blank=True, max_length=250, null=True, verbose_name='work time')),
                ('country', models.CharField(choices=[('AD', 'آندورا'), ('AE', 'امارات متحده عربی'), ('AF', 'افغانستان'), ('AG', 'آنتیگوا و باربودا'), ('AI', 'آنگویلا'), ('AL', 'آلبانی'), ('AM', 'ارمنستان'), ('AO', 'آنگولا'), ('AQ', 'جنوبگان'), ('AR', 'آرژانتین'), ('AS', 'ساموآی آمریکا'), ('AT', 'اتریش'), ('AU', 'استرالیا'), ('AW', 'آروبا'), ('AX', 'جزایر آلند'), ('AZ', 'جمهوری آذربایجان'), ('BA', 'بوسنی و هرزگوین'), ('BB', 'باربادوس'), ('BD', 'بنگلادش'), ('BE', 'بلژیک'), ('BF', 'بورکینا فاسو'), ('BG', 'بلغارستان'), ('BH', 'بحرین'), ('BI', 'بوروندی'), ('BJ', 'بنین'), ('BL', 'سنت بارثلمی'), ('BM', 'برمودا'), ('BN', 'برونئی'), ('BO', 'بولیوی'), ('BQ', 'هلند کارائیب'), ('BR', 'برزیل'), ('BS', 'باهاما'), ('BT', 'بوتان'), ('BV', 'جزیره بووه'), ('BW', 'بوتسوانا'), ('BY', 'بلاروس'), ('BZ', 'بلیز'), ('CA', 'کانادا'), ('CC', 'جزایر کوکوس'), ('CD', 'جمهوری دموکراتیک کنگو'), ('CF', 'جمهوری آفریقای مرکزی'), ('CG', 'جمهوری کنگو'), ('CH', 'سوئیس'), ('CI', 'ساحل عاج'), ('CK', 'جزایر کوک'), ('CL', 'شیلی'), ('CM', 'کامرون'), ('CN', 'چین'), ('CO', 'کلمبیا'), ('CR', 'کاستاریکا'), ('CU', 'کوبا'), ('CV', 'کیپ ورد'), ('CW', 'کوراسائو'), ('CX', 'جزیره کریسمس'), ('CY', 'قبرس'), ('CZ', 'جمهوری چک'), ('DE', 'آلمان'), ('DJ', 'جیبوتی'), ('DK', 'دانمارک'), ('DM', 'دومینیکا'), ('DO', 'دومینیکا'), ('DZ', 'الجزایر'), ('EC', 'اکوادور'), ('EE', 'استونی'), ('EG', 'مصر'), ('EH', 'صحرای غربی'), ('ER', 'اریتره'), ('ES', 'اسپانیا'), ('ET', 'اتیوپی'), ('FI', 'فنلاند'), ('FJ', 'فیجی'), ('FK', 'جزایر فالکلند'), ('FM', 'ایالات فدرال میکرونزی'), ('FO', 'جزایر فارو'), ('FR', 'فرانسه'), ('GA', 'گابن'), ('GB', 'انگلستان'), ('GD', 'گرانادا'), ('GE', 'گرجستان'), ('GF', 'گویان فرانسه'), ('GG', 'گرنزی'), ('GH', 'غنا'), ('GI', 'جبل الطارق'), ('GL', 'گرینلند'), ('GM', 'گامبیا'), ('GN', 'گینه'), ('GP', 'جزیره گوادلوپ'), ('GQ', 'گینه استوایی'), ('GR', 'یونان'), ('GS', 'جزایر جورجیای جنوبی و ساندویچ جنوبی'), ('GT', 'گواتمالا'), ('GU', 'گوام'), ('GW', 'گینه بیسائو'), ('GY', 'گویان'), ('HK', 'هنگ کنگ'), ('HM', 'جزیره هرد و جزایر مک دونالد'), ('HN', 'هندوراس'), ('HR', 'کرواسی'), ('HT', 'هائیتی'), ('HU', 'مجارستان'), ('ID', 'اندونزی'), ('IE', 'جمهوری ایرلند'), ('IL', 'فلسطین اشغالی (اسرائیل)'), ('IM', 'جزیره من'), ('IN', 'هند'), ('IO', 'قلمروی اقیانوس هند بریتانیا'), ('IQ', 'عراق'), ('IR', 'ایران'), ('IS', 'ایسلند'), ('IT', 'ایتالیا'), ('JE', 'ادبیات'), ('JM', 'جامائیکا'), ('JO', 'اردن'), ('JP', 'ژاپن'), ('KE', 'کنیا'), ('KG', 'قرقیزستان'), ('KH', 'کامبوج'), ('KI', 'کیریباتی'), ('KM', 'کومور'), ('KN', 'سنت کیتس و نویس'), ('KP', 'کره شمالی'), ('KR', 'کره جنوبی'), ('KW', 'کویت'), ('KY', 'جزایر کیمن'), ('KZ', 'قزاقستان'), ('LA', 'لائوس'), ('LB', 'لبنان'), ('LC', 'سنت لوسیا'), ('LI', 'لیختن اشتاین'), ('LK', 'سری لانکا'), ('LR', 'لیبریا'), ('LS', 'لسوتو'), ('LT', 'لیتوانی'), ('LU', 'لوکزامبورگ'), ('LV', 'لتونی'), ('LY', 'لیبی'), ('MA', 'مراکش'), ('MC', 'موناکو'), ('MD', 'مولداوی'), ('ME', 'مونته نگرو'), ('MF', 'سنت مارتین فرانسه'), ('MG', 'ماداگاسکار'), ('MH', 'جزایر مارشال'), ('MK', 'جمهوری مقدونیه'), ('ML', 'مالی'), ('MM', 'میانمار'), ('MN', 'مغولستان'), ('MO', 'ماکائو'), ('MP', 'جزایر ماریانای شمالی'), ('MQ', 'مارتینیک'), ('MR', 'موریتانی'), ('MS', 'مونتسرات'), ('MT', 'مالت'), ('MU', 'موریس'), ('MV', 'مالدیو'), ('MW', 'مالاوی'), ('MX', 'مکزیک'), ('MY', 'مالزی'), ('MZ', 'موزامبیک'), ('NA', 'نامیبیا'), ('NC', 'کالدونیای جدید'), ('NE', 'نیجر'), ('NF', 'جزیره نورفولک'), ('NG', 'نیجریه'), ('NI', 'نیکاراگوئه'), ('NL', 'هلند'), ('NO', 'نروژ'), ('NP', 'نپال'), ('NR', 'نائورو'), ('NU', 'نیوئه'), ('NZ', 'نیوزلند'), ('OM', 'عمان'), ('PA', 'پاناما'), ('PE', 'پرو'), ('PF', 'پلینزی فرانسه'), ('PG', 'پاپوآ گینه نو'), ('PH', 'فیلیپین'), ('PK', 'پاکستان'), ('PL', 'لهستان'), ('PM', 'سنت پیر و ماژلان'), ('PN', 'جزایر پیت\u200cکرن'), ('PR', 'پورتوریکو'), ('PS', 'فلسطین'), ('PT', 'پرتغال'), ('PW', 'پالائو'), ('PY', 'پاراگوئه'), ('QA', 'قطر'), ('RE', 'ریونیون'), ('RO', 'رومانی'), ('RS', 'صربستان'), ('RU', 'روسیه'), ('RW', 'رواندا'), ('SA', 'عربستان سعودی'), ('SB', 'جزایر سلیمان'), ('SC', 'سیشل'), ('SD', 'سودان'), ('SE', 'سوئد'), ('SG', 'سنگاپور'), ('SH', 'سینت هلینا'), ('SI', 'اسلوونی'), ('SJ', 'سوالبارد و یان ماین'), ('SK', 'اسلواکی'), ('SL', 'سیرالئون'), ('SM', 'سن مارینو'), ('SN', 'سنگال'), ('SO', 'سومالی'), ('SR', 'سورینام'), ('ST', 'سائوتومه و پرینسیپ'), ('SV', 'السالوادور'), ('SX', 'سنت مارتین هلند'), ('SY', 'سوریه'), ('SZ', 'سوازیلند'), ('TC', 'جزایر تورکس و کایکوس'), ('TD', 'چاد'), ('TF', 'سرزمین\u200cهای قطب جنوب و جنوبی فرانسه'), ('TG', 'توگو'), ('TH', 'تایلند'), ('TJ', 'تاجیکستان'), ('TK', 'توکلائو'), ('TL', 'تیمور شرقی'), ('TM', 'ترکمنستان'), ('TN', 'تونس'), ('TO', 'تونگا'), ('TR', 'ترکیه'), ('TT', 'ترینیداد و توباگو'), ('TV', 'تووالو'), ('TW', 'تایوان'), ('TZ', 'تانزانیا'), ('UA', 'اوکراین'), ('UG', 'اوگاندا'), ('UM', 'جزایر کوچک حاشیه\u200cای آمریکا'), ('US', 'ایالات متحده'), ('UY', 'اروگوئه'), ('UZ', 'ازبکستان'), ('VA', 'شهر واتیکان'), ('VC', 'سنت وینسنت و گرنادین'), ('VE', 'ونزوئلا'), ('VG', 'جزایر ویرجین بریتانیا'), ('VI', 'جزایر ویرجین ایالات متحده آمریکا'), ('VN', 'ویتنام'), ('VU', 'وانواتو'), ('WF', 'والیس و فوتونا'), ('WS', 'ساموآ'), ('YE', 'یمن'), ('YT', 'مایوت'), ('ZA', 'آفریقای جنوبی'), ('ZM', 'زامبیا'), ('ZW', 'زیمبابوه')], default='IR', max_length=100, verbose_name='country')),
                ('province', models.CharField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'), ('اصفهان', 'اصفهان'), ('البرز', 'البرز'), ('ایلام', 'ایلام'), ('بوشهر', 'بوشهر'), ('تهران', 'تهران'), ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'), ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'), ('خراسان شمالی', 'خراسان شمالی'), ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'), ('سمنان', 'سمنان'), ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'), ('قم', 'قم'), ('کردستان', 'کردستان'), ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'), ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'), ('مازندران', 'مازندران'), ('مرکزی', 'مرکزی'), ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'), ('یزد', 'یزد')], max_length=200, verbose_name='province')),
                ('city', models.CharField(max_length=150, verbose_name='city')),
                ('is_company_have_living_place', models.BooleanField(default=False, verbose_name='is company have living place')),
                ('minimum_age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18)], verbose_name='minimum age')),
                ('maximum_age', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(50)], verbose_name='maximum age')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('preferably_male', 'preferably_male'), ('preferably_female', 'preferably_female')], max_length=17, verbose_name='gender')),
                ('military_service_status', models.CharField(choices=[('دارای کارت پایان خدمت', 'دارای کارت پایان خدمت'), ('در حال خدمت', 'در حال خدمت'), ('معافیت پزشکی', 'معافیت پزشکی'), ('سایر معافیت ها( معافیت غیر پزشکی )', 'سایر معافیت ها( معافیت غیر پزشکی )'), ('اهمیتی ندارد', 'اهمیتی ندارد')], max_length=100, verbose_name='Military Service Status')),
                ('work_experience', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)], verbose_name='amount of work experience')),
                ('language', models.CharField(choices=[], max_length=100, verbose_name='languages')),
                ('language_level', models.CharField(choices=[('ضعیف', 'ضعیف'), ('متوسط', 'متوسط'), ('خوب', 'خوب'), ('عالی', 'عالی')], max_length=20, verbose_name='language level')),
                ('benefits', models.CharField(blank=True, choices=[], max_length=200, null=True, verbose_name='benefits')),
                ('salary', models.CharField(choices=[], db_index=True, max_length=75, verbose_name='salary')),
                ('job_description', models.TextField(blank=True, max_length=500, null=True, verbose_name='job description')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='accounts.companyprofile')),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]
