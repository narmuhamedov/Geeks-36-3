from django import forms
from . import models


class TekkenForm(forms.ModelForm):
    class Meta:
        model = models.PersonGame
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'

