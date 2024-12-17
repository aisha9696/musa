from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Author')
    text = forms.CharField(
        max_length=400, required=True,
        label='Text', widget=widgets.Textarea,)
    email = forms.EmailField(
        max_length=40, required=True,
        label='Email',
    )
