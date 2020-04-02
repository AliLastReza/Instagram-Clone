from time import sleep
from kavenegar import *
from celery.task import task
from django.contrib.auth import get_user_model
from instagram.localsetting import Kave_Api
User = get_user_model()


@task(name="Send Verification Code")
def send_verification_code(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExists:
        return None

    return user.username


@task(name="Send Verificaton Email")
def send_verification_email(email):
    sleep(10)
    print("email :", email)


@task(name='Send Sms')
def send_sms_api_kavenegar(username):
    phone_number = User.objects.get(username=username).phone_number
    try:
        api = KavenegarAPI(Kave_Api)
        print(api)
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': 'سلام کاربر {} به سایت ما خوش اومدید'.format(username),
        }
        print(params)
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
