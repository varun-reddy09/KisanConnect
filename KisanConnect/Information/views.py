


from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



import requests
import json

from .models import Profile

# Create your views here.

def home(request):
    return render(request,'information/index.html')


def dashboard(request):
    return render(request,"information/dashboard.html")

def cropinfo(request):
    return render(request,"information/cropinfo.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        emailid = request.POST.get("email")
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobile')
        user = User.objects.create_user(username=emailid, email=emailid, password=password,first_name=username)
        print(user)
        user.is_staff = True
        user.save()

        profile = Profile(user=user, phone_number=mobile_number)
        profile.save()
        login(request, user)
        return redirect(reverse('dashboard'))
        pass
    pass

#login Page
def loginform(request):
    return render(request,"Information/login.html")


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def login_view(request):
    if request.method == 'POST':

        mail=request.POST.get('email')
        pw=request.POST.get('password')
        print(mail,pw)
        user = authenticate(username=mail, password=pw)

        if user is not None:
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return HttpResponse("This User doesn't exist");


def marketprice(request):

    if request.method == 'GET':

        data=requests.get('https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=20&limit=10').json()
        print(data)

        title=data['title']
        org=data['org'][0]
        source=data['source']
        records=data['records']
        value1 = data['records'][0]
        print(value1)
        # value2 = data['records'][1]
        # value3 = data['records'][2]
        # value4 = data['records'][3]
        # value5 = data['records'][4]
        # value6 = data['records'][5]
        # value7 = data['records'][6]
        # value8 = data['records'][7]
        # value9 = data['records'][8]
        # value10 = data['records'][9]

        return render(request,'information/marketprice.html',{'title':title,'org':org,'source':source,'records':records})












