from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.forms import widgets

from accounts.models import Profile


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username', 'password1', 
            'password2', 'first_name', 
            'last_name', 'email',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError("Поле 'Email' должно быть заполнено.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError("Хотя бы одно из полей 'Имя' или 'Фамилия' должно быть заполнено.")

        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
            }),
            'last_name': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
            }),
            'email': widgets.EmailInput(attrs={
                'class': 'form-control mb-3',
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me', 'avatar')
        widgets = {
            'about_me': widgets.TextInput(attrs={
                'class': 'form-control mb-3',
            }),
            'avatar': widgets.FileInput(attrs={
                'class': 'form-control mb-3',
            }),
        }


class ChangePasswordForm(PasswordChangeForm):
    widgets = {
        'new_password1': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3',
        }),
        'new_password2': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3',
        }),
        'old_password': widgets.PasswordInput(attrs={
            'class': 'form-control mb-3',
        }),
    }
