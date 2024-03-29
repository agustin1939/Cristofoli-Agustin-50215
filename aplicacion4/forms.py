from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ServicioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    tiempo = forms.CharField(max_length=40, required=True)


class JuegoForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    consola = forms.CharField(max_length=60, required=True)
    stock = forms.IntegerField(required=True)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):
    first_name = forms.CharField(
        label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(
        label="Apellido/s", max_length=50, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
