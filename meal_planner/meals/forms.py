from datetime import date
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, CheckboxSelectMultiple, \
    ModelMultipleChoiceField
from django.core.exceptions import ValidationError

from meals.models import Breakfast, Lunch, Dinner


class BreakfastForm(ModelForm):
    class Meta:
        model = Breakfast
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'meal': CheckboxSelectMultiple
        }
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meals cannot be in the past!")
        return d

class LunchForm(ModelForm):
    class Meta:
        model = Lunch
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'meal': CheckboxSelectMultiple
        }
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meals cannot be in the past!")
        return d

class DinnerForm(ModelForm):
    class Meta:
        model = Dinner
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'meal': CheckboxSelectMultiple
        }
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meals cannot be in the past!")
        return d