from jalali_date import datetime2jalali
from django.utils import timezone


def persian_date_convertor(time):
    persian_date = datetime2jalali(time).strftime('%y/%m/%d - ساعت %H:%M')
    return persian_date
