from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'image', 'text', 'email']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'email', 'edit_by_admin']
