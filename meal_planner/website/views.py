from django.http import HttpResponse
from django.shortcuts import render
from meals.models import Breakfast, Lunch, Dinner

def welcome(request):
    return render(request, "website/welcome.html",
                  {"breakfast": Breakfast.objects.all(),
                   "lunch": Lunch.objects.all(),
                   "dinner": Dinner.objects.all()})
