from kavenegar import *
from typing import Dict


def send_otp_code(receptor: Dict):
    try:
        api = KavenegarAPI('347469516C65733378573744792F4F3779386D73696C76672F4A65686A3478676E35654C673459667949553D')
        params = {
            'sender': '0018018949161',
            'receptor': receptor.get("receptor"),
            'message': f'کد یکبار مصرف شما : { receptor.get("code") }'
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
        print(str(e))

    except HTTPException as e:
        print(str(e))
