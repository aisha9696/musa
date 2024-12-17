from django import forms
from django.forms import widgets
from webapp.models import Product, Review
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'picture', 'description')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'grade')
