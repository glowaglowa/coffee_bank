from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.views.generic import ListView

from coffee_app.forms import CreateUser

from coffee_app.models import Roastery, Origin, Roast, Coffee, Users, UsersCoffees
from django.contrib import messages


class CoffeesView(ListView):
    template_name = 'coffee_app.html'
    model = Coffee


def coffeeRegisterPage(request):
    if request.user.is_authenticated:
        return redirect('loginPage')
    else:
        formula = CreateUser()
        if request.method == 'POST':
            formula = CreateUser(request.POST)
            if formula.is_valid():
                user = formula.save()
                username = formula.cleaned_data.get('username')
                Users.objects.create(
                    username=user,
                )
                messages.success(request, "Account was successfully created for " + username)

                return redirect('login')

        cond = {'formula': formula}
        return render(request, 'register.html', cond)


def coffeeLoginPage(request):
    formula = AuthenticationForm()
    if request.method == 'POST':
        formula = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('coffee_app')
        else:
            messages.info(request, "Username or password is incorrect")

    cond = {"formula": formula}
    return render(request, 'login.html', cond)


def coffeLogOut(request):
    logout(request)
    return redirect('loginPage')
