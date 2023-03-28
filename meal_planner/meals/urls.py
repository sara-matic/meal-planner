from django.urls import path

from . import views

urlpatterns = [
    path('breakfast/<int:id>', views.breakfast),
    path('lunch/<int:id>', views.lunch),
    path('dinner/<int:id>', views.dinner)
]