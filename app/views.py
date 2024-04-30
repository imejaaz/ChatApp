from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':

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
    
