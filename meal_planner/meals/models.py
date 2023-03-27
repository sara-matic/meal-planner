import calendar

from django.db import models



class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Breakfast(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField(unique=True)

    def __str__(self):
        breakfast = f"Breakfast on {self.date.strftime('%A, %b %d, %Y')}: * "
        for m in self.meal.all():
            breakfast += f"{str(m)} * "
        return breakfast

class Lunch(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField(unique=True)

    def __str__(self):
        lunch = f"Lunch on {self.date.strftime('%A, %b %d, %Y')}: * "
        for m in self.meal.all():
            lunch += f"{str(m)} * "
        return lunch


class Dinner(models.Model):
    meal = models.ManyToManyField(Food)
    date = models.DateField(unique=True)

    def __str__(self):
        dinner = f"Dinner on {self.date.strftime('%A, %b %d, %Y')}: * "
        for m in self.meal.all():
            dinner += f"{str(m)} * "
        return dinner


