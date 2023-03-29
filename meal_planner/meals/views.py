from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
from meals.forms import BreakfastForm, LunchForm, DinnerForm, FoodForm
from meals.models import Breakfast, Lunch, Dinner

from meals.models import Food


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

def new_breakfast(request):
    if request.method == "POST":

        form = BreakfastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = BreakfastForm
    return render(request, "meals/new.html", {"form": form, "meal": "Breakfast"})

def edit_breakfast(request, id):
    breakfast = get_object_or_404(Breakfast, pk=id)
    if request.method == "POST":
        form = BreakfastForm(request.POST, instance=breakfast)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = BreakfastForm(instance=breakfast)
    return render(request, "meals/edit.html", {"form": form, "meal": "Breakfast"})

def delete_breakfast(request, id):
    breakfast = get_object_or_404(Breakfast, pk=id)
    if request.method == "POST":
        breakfast.delete()
        return redirect("welcome")
    return render(request, "meals/confirm.html", {"meal_name": "Breakfast", "meal": breakfast, "view_function_name": "breakfast"})

def new_lunch(request):
    if request.method == "POST":

        form = LunchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = LunchForm
    return render(request, "meals/new.html", {"form": form, "meal": "Lunch"})


def new_dinner(request):
    if request.method == "POST":

        form = DinnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = DinnerForm
    return render(request, "meals/new.html", {"form": form, "meal": "Dinner"})


def all_food(request):
    return render(request, "meals/food.html",
                  {"food": Food.objects.order_by('name')})

def new_food(request):
    if request.method == "POST":

        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("food")

    else:
        form = FoodForm
    return render(request, "meals/new.html", {"form": form, "meal": "Food"})

