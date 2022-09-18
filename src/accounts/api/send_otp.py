import redis

from extensions.otp_services import send_otp_code
from extensions.utils import create_otp_code
from config.settings import REDIS_PORT, HOST_NAME


class OTPSend:
    def __init__(self, received_phone: str, id_code: str):
        self.code: int = create_otp_code()
        self.id_code = id_code
        self.received_phone = received_phone
        self.redis_conf = redis.Redis(
            host=HOST_NAME, port=REDIS_PORT
        )
        self.create_otp(self.code, self.id_code)

    def send_otp(self, code: int):
        pass
        # return send_otp_code(
        #     {
        #         'receptor': f'0{self.received_phone}',
        #         'code': code
        #     }
        # )

    def create_otp(self, code: int, id_code: str):
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

        return self.send_otp(code)

# def send_otp_or_not(received_phone: str) -> Response:
#     otp_code: int = create_otp_code()
#     id_code: str = create_random_code()
#
#     try:
#         OTPDocument.objects.create(
#             code=otp_code,
#             contact=received_phone,
#             id_code=id_code
#         )
#         # send_otp_code(
#         #     {
#         #         'receptor': f'0{received_phone}',
#         #         'code': otp_code
#         #     }
#         # )
#
#         context = {
#             "status": f"send otp to {received_phone}",
#             "id_code": id_code
#         }
#
#         return Response(
#             context,
#             status=status.HTTP_200_OK
#         )
#
#     except IntegrityError:
#         return Response(
#             {
#                 "Has been sent.": "The code has been sent to this number!"
#             },
#             status=status.HTTP_428_PRECONDITION_REQUIRED
#         )
