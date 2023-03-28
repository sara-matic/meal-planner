from django.shortcuts import render, get_object_or_404

from meals.models import Breakfast, Lunch, Dinner
def breakfast(request, id):
    meal = get_object_or_404(Breakfast, pk=id)
    return render(request, "meals/breakfast.html",
                  {"breakfast": meal})

def lunch(request, id):
    meal = get_object_or_404(Lunch, pk=id)
    return render(request, "meals/lunch.html",
                  {"lunch": meal})

def dinner(request, id):
    meal = get_object_or_404(Dinner, pk=id)
    return render(request, "meals/dinner.html",
                  {"dinner": meal})