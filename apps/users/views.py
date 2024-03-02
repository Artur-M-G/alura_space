from django.shortcuts import render, redirect
from .forms import LoginForms, SingUpForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username_login = form['username_login'].value()
            password = form['password'].value()
        
            user = auth.authenticate(
                request,
                username=username_login,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, f'{username_login} successfully logged in!')
                return redirect('index')
            else:
                messages.error(request, 'Error when logging in')
                return redirect('login')

    return  render(request, 'users/login.html', {"form": form})

def singup(request):
    form = SingUpForms()

    if request.method == 'POST':
        form = SingUpForms(request.POST)

        if form.is_valid():
            username_singup = form['username_singup'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=username_singup).exists():
                messages.error(request, 'User already exist')
                return redirect('singup')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail already registered')
                return redirect('singup')
            
            usuario = User.objects.create_user(
                username=username_singup,
                email=email,
                password=password
            )
            usuario.save()
            messages.success(request, 'SingUp successfully Complete!')
            return redirect('login')

    return render(request, 'users/singup.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logout successful!")
    else:
        messages.error(request, "You are not logged in")
    return redirect('login')
