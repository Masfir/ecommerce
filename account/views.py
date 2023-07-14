from django.shortcuts import render,redirect
from .forms import UserSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
# Create your views here.

def user_signup(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(data = request.POST)
        #print(form,"show data")
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form
    }
    return render(request,'account/signup.html',context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    context ={
        'form':form
    }
    return render(request,'account/login.html',context)

def user_logout(request):
    logout(request)
    return redirect('user_signup')


def user_profile_list(request):
    user_profile_query = UserProfile.objects.filter(user = request.user)
    u = User.objects.all()
    print(u)

    context ={
        'user_profile_query':user_profile_query,
        'u':u,
    }
    return render(request,'account/user_profile.html',context)


def update_profile(request):
    update_profile_query = UserProfile.objects.get(user=request.user)
    Update_Profile_Form = UpdateProfileForm(instance=update_profile_query)

    if request.method =='POST':
        print(request.POST)
        Update_Profile_Form = UpdateProfileForm(request.POST,instance=update_profile_query)
        if Update_Profile_Form.is_valid():
            Update_Profile_Form.save()
        return redirect('user_profile_list')
    context ={
        'Update_Profile_Form':Update_Profile_Form,
    }
    return render(request,'account/user_profile_update.html',context)


