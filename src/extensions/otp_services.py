from kavenegar import *
from typing import Dict


def send_otp_code(receptor: Dict):
    try:
        api = KavenegarAPI('79545974732B4249757055495079716775413467797446565769435234317832414F5961573634494A36593D')
        params = {
            'sender': '10004346',
            'receptor': receptor.get("receptor"),
            'message': f'کد یکبار مصرف شما : { receptor.get("code") }'
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
        print(str(e))

    except HTTPException as e:
        print(str(e))
