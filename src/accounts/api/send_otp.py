import redis
from typing import Dict

from rest_framework import status
from rest_framework.response import Response

from extensions.otp_services import send_otp_code
from config.settings import REDIS_PORT, REDIS_HOST_NAME
from extensions.utils import create_otp_code, create_random_code


class OTP:

    def __init__(self, received_phone: str, code: int, id_code: str):
        self.code = code
        self.id_code = id_code
        self.received_phone = received_phone
        self.redis_conf = redis.Redis(
            host=REDIS_HOST_NAME, port=REDIS_PORT
        )
        self.create_otp(self.code, self.id_code)

    def create_otp(self, code, id_code) -> None:
        data = {
            'contact': self.received_phone,
            'code': code,
            'id_code': id_code,
            'retry': 0
        }

        with self.redis_conf.pipeline() as pipe:
            pipe.hset(self.received_phone, mapping=data)
            pipe.expire(self.received_phone, 120)
            pipe.execute()


def send_otp(received_phone):
    code: int = create_otp_code()
    id_code: str = create_random_code()
    # send_otp_code(
    #     {
    #         'receptor': f'0{received_phone}',
    #         'code': CODE
    #     }
    # )

    OTP(received_phone, code, id_code)

    context = {
        "status": f"send otp to {received_phone}",
        "id_code": id_code
    }

    return Response(
        context,
        status=status.HTTP_200_OK
    )
