import random

from django.core.cache import cache
from zeep import Client


def create_random_number():
    return str(random.randint(10000, 999999))


def send_sms(phone, otp=None, message=None):
    username = "09177080841"
    password = "09177080841"
    sender_number = "5000203001397"
    if message:
        message_body = message
    else:
        message_body = (
            f"کدتایید پلاست اپ: {otp}\nهشدار:لطفا این کد را در اختیار کسی قرار ندهید."
        )
    type_of_message = 1
    allowed_delay = 0
    client = Client("https://www.payam-resan.com/ws/v2/ws.asmx?WSDL")
    result = client.service.SendMessage(
        Username=username,
        PassWord=password,
        SenderNumber=sender_number,
        RecipientNumbers=[str(phone)],
        MessageBodie=message_body,
        Type=type_of_message,
        AllowedDelay=allowed_delay,
    )
    return result


def send_otp(phone_number):
    otp = create_random_number()
    print(otp)
    cache.set(f"{phone_number}-for-authentication", otp,10000)
    send_sms(phone_number, otp)
