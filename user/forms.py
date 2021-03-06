from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import My_User

class CreateUser(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite uma senha válida'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita a senha'}),
    )
    class Meta:
        model = My_User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        }

class UpdateUser(UserChangeForm):
    class Meta:
        model = My_User
        fields = ['photo','first_name', 'last_name', 'email', 'bio']