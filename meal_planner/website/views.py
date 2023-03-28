from django.http import HttpResponse
from django.shortcuts import render
from meals.models import Breakfast, Lunch, Dinner

def welcome(request):
    return render(request, "website/welcome.html",
                  {"breakfast": Breakfast.objects.order_by('date'),
                   "lunch": Lunch.objects.order_by('date'),
                   "dinner": Dinner.objects.order_by('date')})

