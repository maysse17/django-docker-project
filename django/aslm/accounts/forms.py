from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm as _UserCreationForm
from django.contrib.auth.forms import AuthenticationForm as _AuthenticationForm


class UserCreationForm(_UserCreationForm):
    """
    A form that creates a user, with privileges, from the given username, first name, last name, email and
    password.
    """
    first_name = forms.CharField(
        label=_('First Name'),
        strip=True
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        strip=True
    )
    email = forms.EmailField(
        label=_('Email')
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AuthenticationForm(_AuthenticationForm):
    pass
