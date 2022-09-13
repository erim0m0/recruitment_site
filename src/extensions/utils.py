from string import digits, ascii_letters
from secrets import choice
import random
from jalali_date import datetime2jalali


def persian_date_convertor(time) -> str:
    persian_date = datetime2jalali(time).strftime('%y/%m/%d - ساعت %H:%M')
    return persian_date


def create_random_code() -> str:
    alphabet = ascii_letters + digits
    random_code: str = ''.join(choice(alphabet) for i in range(32))
    return random_code


def create_otp_code(size: int = 6, char: str = digits) -> int:
    random_otp_code = int(''.join(
        "".join(choice(char) for _ in range(size))
    ))
    return random_otp_code
