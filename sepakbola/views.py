import datetime
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_manage_pertandingan(request):
    context = {
    }
    return render(request, "pages/manage-pertandingan.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_pembuatan_pertandingan(request):
    context = {
    }
    return render(request, "pages/pembuatan-pertandingan.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_form_pemilihan_jadwal(request):
    context = {
    }
    return render(request, "pages/form-pemilihan-jadwal.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_form_pembuatan_pertandingan(request):
    context = {
    }
    return render(request, "pages/form-pembuatan-pertandingan.html", context)

# TODO: ini yang bener, sementara ga pake id dulu
# #@login_required(login_url='/sepakbola/login/')
# def show_peristiwa_tim(request, id):
#     context = {
#         "id": id
#     }
#     return render(request, "pages/peristiwa-tim.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_peristiwa_tim(request):
    context = {
    }
    return render(request, "pages/peristiwa-tim.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/peminjaman-stadium.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_form_peminjaman_stadium(request):
    context = {
    }
    return render(request, "pages/form-peminjaman-stadium.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_list_pertandingan(request):
    context = {
    }
    return render(request, "pages/list-pertandingan.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_history_rapat(request):
    context = {
    }
    return render(request, "pages/history-rapat.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_mengelola_tim(request):
    context = {
    }
    return render(request, "pages/mengelola-tim.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_pilih_pemain(request):
    context = {
    }
    return render(request, "pages/pilih-pemain.html", context)

#@login_required(login_url='/sepakbola/login/')
def show_pilih_pelatih(request):
    context = {
    }
    return render(request, "pages/pilih-pelatih.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
def show_dashboard_manajer(request):
    context = {
    }
    return render(request, "dashboard/dashboard-manajer.html", context)

@csrf_exempt
@login_required(login_url='/sepakbola/login/')
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

# dk start
@login_required(login_url='/sepakbola/login/')
def mulai_rapat(request):
  user = request.user
  context = {
    }
  return render(request, "pages/mulai_rapat.html", context)

@login_required(login_url='/sepakbola/login/')
def mulai_pertandingan(request):
  user = request.user
  context = {
    }
  return render(request, "pages/mulai_pertandingan.html", context)

@login_required(login_url='/sepakbola/login/')
def form_isi_rapat(request):
  user = request.user
  context = {
    }
  return render(request, "pages/form_isi_rapat.html", context)

@login_required(login_url='/sepakbola/login/')
def tim1_peristiwa(request):
  user = request.user
  context = {
    }
  return render(request, "pages/tim1_peristiwa.html", context)

@login_required(login_url='/sepakbola/login/')
def tim2_peristiwa(request):
  user = request.user
  context = {
    }
  return render(request, "pages/tim2_peristiwa.html", context)

@login_required(login_url='/sepakbola/login/')
def pembelian_tiket(request):
  user = request.user
  context = {
    }
  return render(request, "pages/pembelian_tiket.html", context)

@login_required(login_url='/sepakbola/login/')
def pembelian_tiket2(request):
  user = request.user
  context = {
    }
  return render(request, "pages/pembelian_tiket2.html", context)

@login_required(login_url='/sepakbola/login/')
def pembelian_tiket3(request):
  user = request.user
  context = {
    }
  return render(request, "pages/pembelian_tiket3.html", context)

@login_required(login_url='/sepakbola/login/')
def pembelian_tiket4(request):
  user = request.user
  context = {
    }
  return render(request, "pages/pembelian_tiket4.html", context)
# dk end