from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class SignUpForm(forms.Form):
    phone_regex = RegexValidator(
        regex="^9\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("شماره تلفن نامعتبر است.")
    )
    password_regex = RegexValidator(
        regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
        message=_("رمز وارد شده نامعتبر است.")
    )

    phone = forms.CharField(
        max_length=12,
        validators=[phone_regex],
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "logname",
                "class": "form-style",
                "placeholder": "شماره همراه",
                "id": "logname",
                "autocomplete": "off",
            }
        )
    )
    password = forms.CharField(
        validators=[password_regex],
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-style",
                "type": "password",
                "name": "logpass",
                "id": "logpass",
                "placeholder": "Your Password",
                "autocomplete": "off",
                "dir": "ltr"
            }
        )
    )


class OTPCheckForm(forms.Form):
    code = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-style",
                "name": "logpass",
                "id": "logpass",
                "placeholder": "Your Code",
                "autocomplete": "off",
                "dir": "ltr"
            }
        )
    )
