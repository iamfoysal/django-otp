from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Profile
import random
from .helper import send_sms
import json


@csrf_exempt
def home(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        print(response)
        if response['type'] == 'register':
            user = User.objects.create_user(
                username=response['username'], email=response['email'], password=response['password'])
            profile = Profile.objects.create(
                user=user, phone_number=response['phone'])
            otp = random.randint(1000, 9999)
            profile.otp = otp
            profile.save()
            to_phone_number = response['phone']

            message = f'Your otp is {otp}'
            print(message)
            send_sms(to_phone_number, message)
            return HttpResponse('otp sent')

        elif response['type'] == 'otp':
            profile = Profile.objects.get(user__username=response['username'])
            if profile.otp == response['otp']:
                profile.is_verified = True
                profile.save()
                return HttpResponse('otp verified')
            else:
                return HttpResponse('otp not verified')

        elif response['type'] == 'login_otp':
            profile = Profile.objects.get(user__username=response['username'])
            otp = random.randint(1000, 9999)
            profile.otp = otp
            profile.save()
            to_phone_number = profile.phone_number
            message = f'Your login otp is {otp}'
            print(message)
            send_sms(to_phone_number, message)
            return HttpResponse('otp sent')

        elif response['type'] == 'login':
            user = User.objects.get(username=response['username'])
            if user.check_password(response['password']):
                profile = Profile.objects.get(user=user)
                if profile.otp == response['otp']:
                    return HttpResponse('login success')
                else:
                    return HttpResponse('invalid otp')
            else:
                return HttpResponse('invalid password')

        else:
            return HttpResponse('invalid request')
