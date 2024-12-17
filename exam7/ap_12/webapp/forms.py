from django import forms
from django.forms import widgets
from webapp.models import Book, Genre


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'year_of_publishing', 'author', 'description', 'genre')


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
