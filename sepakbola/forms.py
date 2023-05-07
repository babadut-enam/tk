from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    
class RegisterForm(UserCreationForm):
    CHOICES = [('Mahasiswa', 'Mahasiswa'), ('Dosen', 'Dosen'), ('Tendik', 'Tendik'), ('Alumni', 'Alumni'), ('Umum', 'Umum'),]

    username = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    nama_depan = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    nama_belakang = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    nomor_hp = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    email = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    alamat = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    status = forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES)
    )
    jabatan = forms.CharField(
        widget = forms.TextInput(
        attrs={
            "class": "form-control"
        }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nama_depan', 'nama_belakang', 'nomor_hp', 'email',  'status', 'alamat', 'is_manajer', 'is_penonton', 'is_panitia' )