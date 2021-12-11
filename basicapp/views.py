from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.POST.get("email")
    print('entered email ',email)
    o=generateOTP()
    print('otp is= ',o)
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'email by imran',[email],fail_silently=False,html_message=htmlgen)
    # return HttpResponse(o)
    return render(request,o)

def home(request):
    return render(request, "home.html")
