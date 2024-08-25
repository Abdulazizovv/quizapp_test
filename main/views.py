from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def index(request):
    context = {

    }
    return render(request=request, template_name="index.html", context=context)


def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, password=password1)
        user.first_name = full_name
        user.save()
        # Authenticate the user
        authenticated_user = authenticate(username=username, password=password1)
        if authenticated_user is not None:
            login(request, authenticated_user) 
        return redirect('index')
    return render(request, 'reg.html')


def login_(request):
    context = {}
    return render(request, 'login.html', context)