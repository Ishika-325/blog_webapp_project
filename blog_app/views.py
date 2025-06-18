from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')



def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=identifier)
            auth_user = authenticate(request, username=identifier, password=password)
            if auth_user:
                    login(request, auth_user)
                    return redirect('dashboard')
            else:
                    messages.error(request, "Invalid Credentials")
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=identifier)
                auth_user = authenticate(request, username=user.username, password=password)
                if auth_user:
                    login(request, auth_user)
                    return redirect('dashboard')
                else:
                    messages.error(request, "Invalid Credentials")
            except User.DoesNotExist:
                messages.error(request, 'User not found')
                return redirect('signup')
    return render(request, 'blogapp/login/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return redirect('signup')
        
        if password != confirm_password :
            messages.error(request, 'password not match')
            return redirect('signup')
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        login(request, user)
        return redirect('login')
        
        
    return render(request, 'blogapp/login/signup.html')

def forgot_pas(request):
     if request.method == 'POST':
        identifier = request.POST.get('identifier')
        try:
            user = User.objects.get(username=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                messages.error(request, 'User not found')
                return redirect('forgot_pas')
            
        otp=random.randint(100000, 999999)
        print(otp)
        request.session['otp']=otp
        request.session['user_id'] = user.id

        send_mail(
            'password reset for MintBlog',
            f"Your otp for the password reset is {otp}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False
        )
        return redirect('verify_otp')
     return render(request, 'blogapp/login/forgot_pas.html')

def verify_otp(request):
    if request.method=='POST':
        entered_otp = request.POST.get('otp')
        if entered_otp == str(request.session.get('otp')) :
            return redirect('reset_pas')
    return render(request, 'blogapp/login/verify_otp.html')

def reset_pas(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'user not found')
        return redirect('forgot_pas')
    if request.method =='POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password != confirm_password :
            messages.error(request, 'password not match')
            return redirect('reset_pas')
        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        request.session.flush()
        messages.success(request, "password reset successfully . please login")
        return redirect('login')
    return render(request, 'blogapp/login/reset_pas.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'blogapp/dashboard.html')

def blog_detail(request):
    return render(request, 'blogapp/blog_detail.html')

def blog_list(request):
    return render(request, 'blogapp/blog_list.html')

def comments(request):
    return render(request, 'blogapp/comments.html')

def add_blogs(request):
    return render(request, 'blogapp/add_blogs.html')
        

