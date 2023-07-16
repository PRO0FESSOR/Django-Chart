from django.shortcuts import render , HttpResponseRedirect
from .models import Profile
from .forms import LoginForm , ProfileForm
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.

#home
def home(request):
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ProfileForm()
    date = datetime.datetime.now()
    value = date.strftime("%d-%m-%Y")
    value1 = date.strftime("%H:%M")
    profile = Profile.objects.all()
    return render(request,'myapp/home.html',{"profile":profile,"form": form,"date":value,"time":value1})

#loginform

def user_login(request):
    if request.method=="POST":
        form = LoginForm(request=request , data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/') 
    else:
        form = LoginForm()
    return render(request,'myapp/login.html',{"form":form})


