from django.urls import path

from . import views

urlpatterns = [
    path('breakfast/<int:id>', views.breakfast, name='breakfast'),
    path('lunch/<int:id>', views.lunch, name='lunch'),
    path('dinner/<int:id>', views.dinner, name='dinner')
]