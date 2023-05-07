import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def show_home(request):
    context = {
        'nama': 'Daffa',
    }
    return render(request, "home.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/peminjaman_stadium.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_form_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/form_peminjaman_stadium.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_mengelola_tim(request):
    context = {
    }
    return render(request, "pages/mengelola_tim.html", context)


#@login_required(login_url='/sepakbola/login/')
def show_dashboard(request):
    context = {
    }
    return render(request, "dashboard.html", context)

def register(request):
    context = {
    }
    return render(request, "register.html", context)

def register_panitia(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('sepakbola:login')
        else:
            messages.error(request, 'Form tidak valid')
    
    context = {'form': form}
    return render(request, 'register-panitia.html', context)

def register_manajer_penonton(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('sepakbola:login')
        else:
            messages.error(request, 'Form tidak valid')

    context = {'form': form}
    return render(request, 'register-manajer-penonton.html', context)

def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user) # melakukan login terlebih dahulu
                response = HttpResponseRedirect(reverse("sepakbola:dashboard")) # membuat response
                response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
                return response
            else:
                messages.info(request, 'Username atau Password salah!')
        else:
            messages.error(request, 'Form tidak valid')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sepakbola:login'))
    response.delete_cookie('last_login')
    return response
