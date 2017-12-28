from django import forms
from .models import SingleResponse

class ResponseForm(forms.ModelForm):
    class Meta:
        model = SingleResponse
        fields = ['email', 'building', 'room', 'temp','comment']
