import django.db.utils
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from accounts.forms import SignUpForm, OTPCheckForm
from django.urls import reverse_lazy
from .models.blocked_phones import BlockedPhone
from .models import OTP_codes
from extensions.utils import create_otp_code
from django.contrib.auth import get_user_model
from django.core.cache import cache
from datetime import timedelta, datetime
import pytz
from django.utils import timezone
from django.db.models import F
from extensions.otp_services import send_otp_code


class SignUpView(FormView):
    template_name = 'accounts/loguser.html'
    form_class = SignUpForm
    success_url = reverse_lazy('OTP_check')

    def __init__(self, *args, **kwargs):
        return super(SignUpView, self).__init__(*args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        return super(SignUpView, self).get_form_kwargs(**kwargs)

    def form_valid(self, form):
        phone_user = form.cleaned_data.get('phone')
        pass_user = form.cleaned_data.get('password')
        otp_code = create_otp_code()

        try:
            is_blocked_phone = BlockedPhone.objects.get(phone=phone_user)

        except BlockedPhone.DoesNotExist:
            try:
                OTP_codes.OTPDocument.objects.create(
                    code=otp_code, contact=phone_user
                )
                send_otp_code({
                    'receptor': f'0{phone_user}',
                    'code': otp_code
                })
                cache.set('otp_code', otp_code, 120)
                cache.set('pass_user', pass_user, 120)

            except django.db.utils.IntegrityError:
                # todo add message error
                pass

        return super(SignUpView, self).form_valid(form)


class OTPCheckView(FormView):
    template_name = 'accounts/otp_check.html'
    form_class = OTPCheckForm
    success_url = reverse_lazy('signUp-In')

    def form_valid(self, form):
        # main_code = cache.get('otp_code')
        received_code = form.cleaned_data.get('code')
        password = cache.get('password')
        otp = cache.get('otp_code')
        try:
            main_code = OTP_codes.OTPDocument.objects.get(code=received_code)
            is_expired_time = (timezone.now() - timedelta(minutes=2)) <= main_code.create_at
            if is_expired_time:
                if main_code.code == received_code:

                    user = get_user_model()(phone=main_code.contact)
                    user.set_password(password)
                    user.save()
                    main_code.delete()
                else:
                    # todo add not equal_codes error
                    pass
            else:
                cache.delete(password)
                cache.delete(otp)
                # todo add expired_time error
                pass

        except OTP_codes.OTPDocument.DoesNotExist:
            OTP_codes.OTPDocument.objects.filter(code=otp).update(retry=F('retry') + 1)
            return redirect('OTP_check')

        return super(OTPCheckView, self).form_valid(form)
