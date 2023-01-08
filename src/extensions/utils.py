from secrets import choice
from jalali_date import datetime2jalali
from string import digits, ascii_letters
from django.core.exceptions import ValidationError


def persian_date_convertor(time) -> str:
    persian_date = datetime2jalali(time).strftime('%y/%m/%d - %H:%M')
    return persian_date


def create_random_code(amount=32) -> str:
    alphabet = ascii_letters + digits
    random_code: str = ''.join(choice(alphabet) for _ in range(amount))
    return random_code


def create_otp_code(size: int = 6, char: str = digits) -> int:
    random_otp_code = int(''.join(
        "".join(choice(char) for _ in range(size))
    ))
    return random_otp_code


def phone_validator(value: str) -> str:
    from re import match

    if not match("^9\d{2}\s*?\d{3}\s*?\d{4}$", value):
        raise ValidationError(
            "The phone number is Invalid."
        )
    return value


def email_validator(value: str) -> str:
    from re import match

    if not match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value):
        raise ValidationError(
            "The email is Invalid."
        )
    return value


def national_code_validator(value: str) -> str:
    _sum = 0
    for i in range(2, 11):
        _sum += i * int(value[-i])
    last_value, remainder = int(value[-1]), _sum % 11
    if any([2 > remainder == last_value, 11 - remainder == last_value]):
        return value
    raise ValidationError(
        "The national_code is Invalid."
    )


def url_validator(url: str) -> str:
    from re import match

    if not match(
            "^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$",
            url
    ):
        raise ValidationError(
            "The email is Invalid."
        )
    return url
