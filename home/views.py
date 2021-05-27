from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Career
from django.contrib.messages import constants as messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact= Contact(name=name, email=email, phone=phone, message= message, date= datetime.today())
        contact.save()
        #messages.success(request, 'Your message sent succesfully.')
    return render(request, 'index.html')
    #return HttpResponse("This is home page")

def career(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hiring = request.POST.get('hiring')
        video = request.POST.get('video')
        career= Career(fname=fname, lname=lname, email=email, phone=phone, hiring= hiring, video=video, date= datetime.today())
        career.save()
    return render(request, "career.html")

def inner_page(request):
    return render(request, 'inner_page.html')