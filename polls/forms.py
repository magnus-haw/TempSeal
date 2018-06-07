from django import forms
from django.db import models
from .models import SingleResponse, foodResponse

class FoodForm(forms.ModelForm):
    class Meta:
            model = foodResponse
            fields = ['email', 'building', 'room', 'food', 'endTime']
            exclude = ['temp']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = SingleResponse
        fields = ['email', 'building', 'room', 'temp','comment']

