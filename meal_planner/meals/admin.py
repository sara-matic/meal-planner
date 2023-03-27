from django.contrib import admin

from .models import Food, Breakfast, Lunch, Dinner

admin.site.register(Food)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)