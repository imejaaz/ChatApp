from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':

        if 'login_username' in request.POST:
            username = request.POST.get('login_username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return render(request, 'homepage.html')

        else:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            print(username)
            print(email)
            print(password)
            user = User.objects.create_user(username, email, password)
            return redirect('home')
        

    return render(request, 'login.html')
    
