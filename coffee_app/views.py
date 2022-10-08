from django.shortcuts import render
from django.views.generic import ListView

from coffee_app.models import Roastery, Origin, Roast, Coffee, Users, UsersCoffees


class CoffeesView(ListView):
    template_name = 'coffee_app.html'
    model = Coffee
