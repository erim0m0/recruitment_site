import django.db.utils
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from accounts.forms import SignUpForm, OTPCheckForm
from django.urls import reverse_lazy
from .models import OTP_doc, blocked_phones
from extensions.utils import create_otp_code
from django.contrib.auth import get_user_model
from django.core.cache import cache
from datetime import timedelta, datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import F
from extensions.otp_services import send_otp_code
from django.contrib import messages


class SignUpView(FormView):
    template_name = 'accounts/loguser.html'
    form_class = SignUpForm
    success_url = reverse_lazy('OTP_check')

    def __init__(self, *args, **kwargs):
        return super(SignUpView, self).__init__(*args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        return super(SignUpView, self).get_form_kwargs(**kwargs)

    def form_valid(self, form):
        form_valid = super(SignUpView, self).form_valid(form)
        received_phone = form.cleaned_data.get('phone')
        received_password = form.cleaned_data.get('password')
        is_exist_user = get_user_model().objects.filter(phone=received_phone).exists()
        if is_exist_user:
            print('این شماره موجود است')
            return redirect(reverse_lazy('signUp-In'))
        try:
            is_blocked_phone = blocked_phones.BlockedPhone.objects.get(phone=received_phone)
            # messages.error(self.request, _("شماره همراه نامعتبر است."))
            # todo add message
            return redirect(reverse_lazy('signUp-In'))

        except ObjectDoesNotExist:
            otp_code = create_otp_code()

            try:
                OTP_doc.OTPDocument.objects.create(
                    code=otp_code, contact=received_phone
                )
                # send_otp_code({
                #     'receptor': f'0{phone_user}',
                #     'code': otp_code
                # })
                # todo send OTP code
                cache.set('otp_code', otp_code, 120)
                cache.set('pass_user', received_password, 120)
                return form_valid

            except django.db.utils.IntegrityError:
                messages.error(self.request, _("کد یکبار مصرف برای شما ارسال شده است."))
                return redirect(reverse_lazy('OTP_check'))


class OTPCheckView(FormView):
    template_name = 'accounts/otp_check.html'
    form_class = OTPCheckForm
    success_url = reverse_lazy('signUp-In')

    def form_valid(self, form):
        received_code = form.cleaned_data.get('code')
        password = cache.get('pass_user')
        otp = cache.get('otp_code')
        try:
            main_code = OTP_doc.OTPDocument.objects.get(code=received_code)
            is_expired_time = (timezone.now() - timedelta(minutes=2)) > main_code.create_at
            if not is_expired_time:
                user = get_user_model()(phone=main_code.contact)
                user.set_password(password)
                user.save()
                main_code.delete()
                return redirect(reverse_lazy('OTP_check'))
            else:
                main_code.delete()
                cache.delete(password)
                cache.delete(otp)
                messages.error(self.request, _("کد منقضی شده است."))
                print("کد منقضی شده است.")
                return redirect(reverse_lazy('OTP_check'))

        except ObjectDoesNotExist:
            OTP_doc.OTPDocument.objects.filter(code=otp).update(retry=F('retry') + 1)
            main_code = OTP_doc.OTPDocument.objects.get(code=otp)
            if main_code.retry > 4:
                main_code.delete()
                messages.error(self.request, _("تعداد دفعات واردشده بی از حد مجاز"))
                print('ارسال مجدد')
            messages.error(self.request, _("کد وارد شده نادرست می باشد."))
            print('کد وارد شده اشتباه اسن.')
            return redirect(reverse_lazy('OTP_check'))

        return super(OTPCheckView, self).form_valid(form)


def send_otp_code_again(request, contact):
    otp_code = create_otp_code()
    send_otp_code({
        'receptor': f'0{contact}',
        'code': otp_code
    })
    cache.set('otp_code', otp_code, 120)
    cache.set('pass_user', received_password, 120)
    return render(request, 'accounts/otp_check.html')
