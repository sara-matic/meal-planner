from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)

class Breakfast(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField()

class Lunch(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField()

class Dinner(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField()


