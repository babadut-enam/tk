import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def show_home(request):
    context = {
        'nama': 'Daffa',
    }
    return render(request, "home.html", context)

@login_required(login_url='/sepakbola/login/')
def show_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/peminjaman_stadium.html", context)

@login_required(login_url='/sepakbola/login/')
def show_form_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/form_peminjaman_stadium.html", context)

# @login_required(login_url='/sepakbola/login/')
def show_dashboard(request):
    context = {
    }
    return render(request, "dashboard.html", context)

def register(request):
    context = {
    }
    return render(request, "register.html", context)

def register_panitia(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('sepakbola:login')
    
    context = {'form':form}
    return render(request, 'register-panitia.html', context)

def register_manajer_penonton(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('sepakbola:login')
    
    context = {'form':form}
    return render(request, 'register-manajer-penonton.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("sepakbola:dashboard")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('sepakbola:login'))
    response.delete_cookie('last_login')
    return response
