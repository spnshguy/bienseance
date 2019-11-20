# users/forms.py

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import User


class UserAdminForm(forms.ModelForm):
    model = User
    fields = 'username', ' email', 'password', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("Invalid username or password"),
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = _('Email')
        self.fields['password'].label = _('Password')
        self.fields['username'].error_messages = {'required': _('This field is required.')}
        self.fields['password'].error_messages = {'required': _('This field is required.')}

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError({'username': self.error_messages['invalid_login']})
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
