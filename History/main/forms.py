from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from main.models import Scores, Choice


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=16, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': "Логин"
                                                                                           }))
    password = forms.CharField(label='Пароль', max_length=24, widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                                'placeholder': "Пароль",
                                                                                                }))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=16, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': "Логин"
                                                                                           }))
    first_name = forms.CharField(label='Имя', max_length=16, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': "Имя"
                                                                                           }))
    last_name = forms.CharField(label='Фамилия', max_length=24, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                              'placeholder': "Фамилия"
                                                                                              }))

    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input',
                                                                          'placeholder': "Email"}))
    password1 = forms.CharField(label='Пароль', max_length=24,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': "Пароль",
                                                                  }))
    password2 = forms.CharField(label='Повтор пароля', max_length=24,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': "Повтор пароля",
                                                                  }))
    field_order = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}


