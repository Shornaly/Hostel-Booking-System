from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import render, HttpResponse
from staff.models import contactModel,studentModel,BookingModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone_number')
        content=request.POST.get('Content')
        print(name)
        print(phone)
        print(content)
        obj = BookingModel.objects.create(name = name,phone = phone,content = content)
        obj.save()
        if obj:
            print(obj)
        else:
            print("Object not created")
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
    # form = CreateUser()
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     password=request.POST.get('password1')

    #     user_obj=User.objects.create(username=username,password=password)
    #     print(user_obj)



    return render(request, 'login.html')
def booking(request):
    if request.method=="POST":
        Fullname=request.POST.get('Fullname')
        Phone=request.POST.get('Phone')
        Room=request.POST.get('Room')
        Email=request.POST.get('Email')
        Category=request.POST.get('Category')
        print(Fullname)
        print(Phone)
        print(Room)
        print(Email)
        print(Category)
        obj = BookingModel.objects.create(name = Fullname,phone = Phone,room = Room,email = Email,category = Category)
        if obj:
            print(obj)
            return HttpResponseRedirect(reverse('BookingListView'))
        else:
            print("Object not created")
    return render(request, 'booking.html')

def BookingListView(request):
    Bookings= BookingModel.objects.all().order_by('-pk')
    context={
        'Bookings':Bookings
    }
    return render(request,'bookinghistory.html',context)