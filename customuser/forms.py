from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',  'password1', 'password2', 'phone')
        error_messages = {
            'email': {
                'unique': "Указанный адрес уже кем-то используется",
            }, }


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone' )

        error_messages = {
             'email': {
                 'unique': "Указанный адрес уже кем-то используется",
             },}
