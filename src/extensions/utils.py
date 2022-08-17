import string
from django.utils.timezone import localtime
from jalali_date import datetime2jalali
from datetime import datetime, timedelta
import random


def persian_date_convertor(time) -> str:
    persian_date = datetime2jalali(time).strftime('%y/%m/%d - ساعت %H:%M')
    return persian_date


def create_random_code() -> str:
    random_active_code: str = ''.join(
        random.choice(string.ascii_letters + string.digits + '$^&*)(*-') for i in range(72)
    )
    return random_active_code


def create_otp_code() -> int:
    random_otp_code: int = random.randint(111111, 999999)
    return random_otp_code
