from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError

from accounts.models import OTP_doc
from extensions.otp_services import send_otp_code
from extensions.utils import create_otp_code, create_random_code


def send_otp_or_not(received_phone: str):
    try:
        otp_code: int = create_otp_code()
        id_code: str = create_random_code()
        OTP_doc.OTPDocument.objects.create(
            code=otp_code,
            contact=received_phone,
            id_code=id_code
        )
        # send_otp_code({
        #     'receptor': f'0{received_phone}',
        #     'code': otp_code
        # })

        context = {
            "status": f"send otp to {received_phone}",
            "id_code": id_code
        }

        return Response(
            context,
            status=status.HTTP_200_OK
        )

    except IntegrityError:
        return Response(
            {
                "Has been sent.": "The code has been sent to this number!"
            },
            status=status.HTTP_428_PRECONDITION_REQUIRED
        )
