from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def index(request):
    return render(request, 'account/index.html')


def signup(request):
    if request.method == 'POST':

        if 'login_username' in request.POST:
            username = request.POST.get('login_username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('Login successfully')
                return redirect('/post/')
            print('invalid input')
            return HttpResponse("invalid input")

        if 'email' in request.POST:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password != confirm_password:
                print('password does not match!')
                return HttpResponse('password is not same')
            user = User.objects.create_user(username, email, password)
            print('Register successfully')
            return redirect('signup')

    return render(request, 'account/login.html')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('signup')

def profile_view(request):
    return render(request, 'account/profile.html')