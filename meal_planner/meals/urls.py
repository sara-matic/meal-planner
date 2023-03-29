from django.urls import path

from . import views

urlpatterns = [
    path('breakfast/<int:id>', views.breakfast, name='breakfast'),
    path('lunch/<int:id>', views.lunch, name='lunch'),
    path('dinner/<int:id>', views.dinner, name='dinner'),
    path('breakfast/new', views.new_breakfast, name="new_breakfast"),
    path('breakfast/edit/<int:id>', views.edit_breakfast, name="edit_breakfast"),
    path('breakfast/delete/<int:id>', views.delete_breakfast, name="delete"),
    path('lunch/new', views.new_lunch, name="new_lunch"),
    path('dinner/new', views.new_dinner, name="new_dinner"),
    path('food/', views.all_food, name="food"),
    path('food/new', views.new_food, name="new_food")
]