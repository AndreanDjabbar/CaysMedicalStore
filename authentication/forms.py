from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Input Username"
            }
        )
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Input Password"
            }
        )
    )

class RegisterForm(UserCreationForm):
    is_agree = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                "class":"form-check-input"
            }
        )
    )
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "is_agree"
        ]
        widgets = {
            "password1":forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input password"
                }
            ),
            "password2":forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Input Confirmation password"
                }
            )
        }