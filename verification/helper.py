from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import *
from django.conf import settings
from twilio.rest import Client
User = get_user_model()


def send_sms(to_phone_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        messaging_service_sid=settings.TWILIO_SERVICE_SID,
        to=to_phone_number
    )
    print(message.sid)
    return message.sid

    

#  ACf8fe093237be7b27b6d185ec4bf1ff7f
# c77c4c20842ac6e2e476334d8b1a33d7