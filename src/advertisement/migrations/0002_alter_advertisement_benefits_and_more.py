# Generated by Django 4.1 on 2022-12-20 17:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='benefits',
            field=models.CharField(blank=True, choices=[], max_length=200, verbose_name='Benefits'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='city',
            field=models.CharField(max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='country',
            field=models.CharField(choices=[('AD', 'آندورا'), ('AE', 'امارات متحده عربی'), ('AF', 'افغانستان'), ('AG', 'آنتیگوا و باربودا'), ('AI', 'آنگویلا'), ('AL', 'آلبانی'), ('AM', 'ارمنستان'), ('AO', 'آنگولا'), ('AQ', 'جنوبگان'), ('AR', 'آرژانتین'), ('AS', 'ساموآی آمریکا'), ('AT', 'اتریش'), ('AU', 'استرالیا'), ('AW', 'آروبا'), ('AX', 'جزایر آلند'), ('AZ', 'جمهوری آذربایجان'), ('BA', 'بوسنی و هرزگوین'), ('BB', 'باربادوس'), ('BD', 'بنگلادش'), ('BE', 'بلژیک'), ('BF', 'بورکینا فاسو'), ('BG', 'بلغارستان'), ('BH', 'بحرین'), ('BI', 'بوروندی'), ('BJ', 'بنین'), ('BL', 'سنت بارثلمی'), ('BM', 'برمودا'), ('BN', 'برونئی'), ('BO', 'بولیوی'), ('BQ', 'هلند کارائیب'), ('BR', 'برزیل'), ('BS', 'باهاما'), ('BT', 'بوتان'), ('BV', 'جزیره بووه'), ('BW', 'بوتسوانا'), ('BY', 'بلاروس'), ('BZ', 'بلیز'), ('CA', 'کانادا'), ('CC', 'جزایر کوکوس'), ('CD', 'جمهوری دموکراتیک کنگو'), ('CF', 'جمهوری آفریقای مرکزی'), ('CG', 'جمهوری کنگو'), ('CH', 'سوئیس'), ('CI', 'ساحل عاج'), ('CK', 'جزایر کوک'), ('CL', 'شیلی'), ('CM', 'کامرون'), ('CN', 'چین'), ('CO', 'کلمبیا'), ('CR', 'کاستاریکا'), ('CU', 'کوبا'), ('CV', 'کیپ ورد'), ('CW', 'کوراسائو'), ('CX', 'جزیره کریسمس'), ('CY', 'قبرس'), ('CZ', 'جمهوری چک'), ('DE', 'آلمان'), ('DJ', 'جیبوتی'), ('DK', 'دانمارک'), ('DM', 'دومینیکا'), ('DO', 'دومینیکا'), ('DZ', 'الجزایر'), ('EC', 'اکوادور'), ('EE', 'استونی'), ('EG', 'مصر'), ('EH', 'صحرای غربی'), ('ER', 'اریتره'), ('ES', 'اسپانیا'), ('ET', 'اتیوپی'), ('FI', 'فنلاند'), ('FJ', 'فیجی'), ('FK', 'جزایر فالکلند'), ('FM', 'ایالات فدرال میکرونزی'), ('FO', 'جزایر فارو'), ('FR', 'فرانسه'), ('GA', 'گابن'), ('GB', 'انگلستان'), ('GD', 'گرانادا'), ('GE', 'گرجستان'), ('GF', 'گویان فرانسه'), ('GG', 'گرنزی'), ('GH', 'غنا'), ('GI', 'جبل الطارق'), ('GL', 'گرینلند'), ('GM', 'گامبیا'), ('GN', 'گینه'), ('GP', 'جزیره گوادلوپ'), ('GQ', 'گینه استوایی'), ('GR', 'یونان'), ('GS', 'جزایر جورجیای جنوبی و ساندویچ جنوبی'), ('GT', 'گواتمالا'), ('GU', 'گوام'), ('GW', 'گینه بیسائو'), ('GY', 'گویان'), ('HK', 'هنگ کنگ'), ('HM', 'جزیره هرد و جزایر مک دونالد'), ('HN', 'هندوراس'), ('HR', 'کرواسی'), ('HT', 'هائیتی'), ('HU', 'مجارستان'), ('ID', 'اندونزی'), ('IE', 'جمهوری ایرلند'), ('IL', 'فلسطین اشغالی (اسرائیل)'), ('IM', 'جزیره من'), ('IN', 'هند'), ('IO', 'قلمروی اقیانوس هند بریتانیا'), ('IQ', 'عراق'), ('IR', 'ایران'), ('IS', 'ایسلند'), ('IT', 'ایتالیا'), ('JE', 'ادبیات'), ('JM', 'جامائیکا'), ('JO', 'اردن'), ('JP', 'ژاپن'), ('KE', 'کنیا'), ('KG', 'قرقیزستان'), ('KH', 'کامبوج'), ('KI', 'کیریباتی'), ('KM', 'کومور'), ('KN', 'سنت کیتس و نویس'), ('KP', 'کره شمالی'), ('KR', 'کره جنوبی'), ('KW', 'کویت'), ('KY', 'جزایر کیمن'), ('KZ', 'قزاقستان'), ('LA', 'لائوس'), ('LB', 'لبنان'), ('LC', 'سنت لوسیا'), ('LI', 'لیختن اشتاین'), ('LK', 'سری لانکا'), ('LR', 'لیبریا'), ('LS', 'لسوتو'), ('LT', 'لیتوانی'), ('LU', 'لوکزامبورگ'), ('LV', 'لتونی'), ('LY', 'لیبی'), ('MA', 'مراکش'), ('MC', 'موناکو'), ('MD', 'مولداوی'), ('ME', 'مونته نگرو'), ('MF', 'سنت مارتین فرانسه'), ('MG', 'ماداگاسکار'), ('MH', 'جزایر مارشال'), ('MK', 'جمهوری مقدونیه'), ('ML', 'مالی'), ('MM', 'میانمار'), ('MN', 'مغولستان'), ('MO', 'ماکائو'), ('MP', 'جزایر ماریانای شمالی'), ('MQ', 'مارتینیک'), ('MR', 'موریتانی'), ('MS', 'مونتسرات'), ('MT', 'مالت'), ('MU', 'موریس'), ('MV', 'مالدیو'), ('MW', 'مالاوی'), ('MX', 'مکزیک'), ('MY', 'مالزی'), ('MZ', 'موزامبیک'), ('NA', 'نامیبیا'), ('NC', 'کالدونیای جدید'), ('NE', 'نیجر'), ('NF', 'جزیره نورفولک'), ('NG', 'نیجریه'), ('NI', 'نیکاراگوئه'), ('NL', 'هلند'), ('NO', 'نروژ'), ('NP', 'نپال'), ('NR', 'نائورو'), ('NU', 'نیوئه'), ('NZ', 'نیوزلند'), ('OM', 'عمان'), ('PA', 'پاناما'), ('PE', 'پرو'), ('PF', 'پلینزی فرانسه'), ('PG', 'پاپوآ گینه نو'), ('PH', 'فیلیپین'), ('PK', 'پاکستان'), ('PL', 'لهستان'), ('PM', 'سنت پیر و ماژلان'), ('PN', 'جزایر پیت\u200cکرن'), ('PR', 'پورتوریکو'), ('PS', 'فلسطین'), ('PT', 'پرتغال'), ('PW', 'پالائو'), ('PY', 'پاراگوئه'), ('QA', 'قطر'), ('RE', 'ریونیون'), ('RO', 'رومانی'), ('RS', 'صربستان'), ('RU', 'روسیه'), ('RW', 'رواندا'), ('SA', 'عربستان سعودی'), ('SB', 'جزایر سلیمان'), ('SC', 'سیشل'), ('SD', 'سودان'), ('SE', 'سوئد'), ('SG', 'سنگاپور'), ('SH', 'سینت هلینا'), ('SI', 'اسلوونی'), ('SJ', 'سوالبارد و یان ماین'), ('SK', 'اسلواکی'), ('SL', 'سیرالئون'), ('SM', 'سن مارینو'), ('SN', 'سنگال'), ('SO', 'سومالی'), ('SR', 'سورینام'), ('ST', 'سائوتومه و پرینسیپ'), ('SV', 'السالوادور'), ('SX', 'سنت مارتین هلند'), ('SY', 'سوریه'), ('SZ', 'سوازیلند'), ('TC', 'جزایر تورکس و کایکوس'), ('TD', 'چاد'), ('TF', 'سرزمین\u200cهای قطب جنوب و جنوبی فرانسه'), ('TG', 'توگو'), ('TH', 'تایلند'), ('TJ', 'تاجیکستان'), ('TK', 'توکلائو'), ('TL', 'تیمور شرقی'), ('TM', 'ترکمنستان'), ('TN', 'تونس'), ('TO', 'تونگا'), ('TR', 'ترکیه'), ('TT', 'ترینیداد و توباگو'), ('TV', 'تووالو'), ('TW', 'تایوان'), ('TZ', 'تانزانیا'), ('UA', 'اوکراین'), ('UG', 'اوگاندا'), ('UM', 'جزایر کوچک حاشیه\u200cای آمریکا'), ('US', 'ایالات متحده'), ('UY', 'اروگوئه'), ('UZ', 'ازبکستان'), ('VA', 'شهر واتیکان'), ('VC', 'سنت وینسنت و گرنادین'), ('VE', 'ونزوئلا'), ('VG', 'جزایر ویرجین بریتانیا'), ('VI', 'جزایر ویرجین ایالات متحده آمریکا'), ('VN', 'ویتنام'), ('VU', 'وانواتو'), ('WF', 'والیس و فوتونا'), ('WS', 'ساموآ'), ('YE', 'یمن'), ('YT', 'مایوت'), ('ZA', 'آفریقای جنوبی'), ('ZM', 'زامبیا'), ('ZW', 'زیمبابوه')], default='IR', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='gender',
            field=models.CharField(choices=[('male', 'مرد'), ('female', 'زن'), ('preferably_male', 'ترجیحا مرد'), ('preferably_female', 'ترجیحا زن')], max_length=17, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='is_company_have_living_place',
            field=models.BooleanField(default=False, verbose_name='Is company have living place'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='job_description',
            field=models.TextField(blank=True, max_length=400, verbose_name='Job Description'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='language',
            field=models.CharField(choices=[], max_length=100, verbose_name='Languages'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='language_level',
            field=models.CharField(choices=[('ضعیف', 'ضعیف'), ('متوسط', 'متوسط'), ('خوب', 'خوب'), ('عالی', 'عالی')], max_length=5, verbose_name='language level'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='maximum_age',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Maximum age'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='military_service_status',
            field=models.CharField(choices=[('دارای کارت پایان خدمت', 'دارای کارت پایان خدمت'), ('در حال خدمت', 'در حال خدمت'), ('معافیت پزشکی', 'معافیت پزشکی'), ('سایر معافیت ها( معافیت غیر پزشکی )', 'سایر معافیت ها( معافیت غیر پزشکی )'), ('اهمیتی ندارد', 'اهمیتی ندارد')], max_length=34, verbose_name='Military Service Status'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='minimum_age',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(18)], verbose_name='Minimum age'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='province',
            field=models.CharField(choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'), ('اصفهان', 'اصفهان'), ('البرز', 'البرز'), ('ایلام', 'ایلام'), ('بوشهر', 'بوشهر'), ('تهران', 'تهران'), ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'), ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'), ('خراسان شمالی', 'خراسان شمالی'), ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'), ('سمنان', 'سمنان'), ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'), ('قم', 'قم'), ('کردستان', 'کردستان'), ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'), ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'), ('مازندران', 'مازندران'), ('مرکزی', 'مرکزی'), ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'), ('یزد', 'یزد')], max_length=19, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='salary',
            field=models.CharField(choices=[], db_index=True, max_length=75, verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='type_of_cooperation',
            field=models.CharField(choices=[('full-time', 'تمام وقت'), ('per time', 'پاره وقت'), ('remote', 'دورکاری')], max_length=9, verbose_name='type of cooperation'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='work_experience',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(2)], verbose_name='amount of work experience'),
        ),
    ]