from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render

# Create your views here.

# Account Creation
def signup(request):

    if request.method == 'GET':

        return render(request, 'login/signup.html', {
            'form': UserCreationForm
        })

    else:

        if request.POST['password1'] == request.POST['password2']:

            try:
                # Register User
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                return redirect('index')

            except IntegrityError:
                # Failed Register
                return render(request, 'login/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Nombre de usuario ya existe'
                })

        return render(request, 'login/signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


# Logout Account
@login_required
def signout(request):

    logout(request)
    return redirect('index')


# Login Account
def signin(request):

    if request.method == 'GET':

        return render(request, 'login/signin.html', {
            'form': AuthenticationForm
        })

    else:

        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login/signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })

        else:

            login(request, user)
            return redirect('index')
        