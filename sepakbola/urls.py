from sepakbola.views import show_home, register, login_user, logout_user
from sepakbola.views import show_peminjaman_stadium, show_dashboard, show_form_peminjaman_stadium, show_manage_pertandingan
from sepakbola.views import register_manajer_penonton, register_panitia
from django.urls import path

app_name = 'sepakbola'

urlpatterns = [
    path('', show_home, name='home'),
    path('register/', register, name='register'),
    path('register-manajer-penonton/', register_manajer_penonton, name='register-manajer-penonton'),
    path('register-panitia/', register_panitia, name='register-panitia'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('peminjaman-stadium/', show_peminjaman_stadium, name='peminjaman_stadium'),
    path('manage-pertandingan/', show_manage_pertandingan, name='manage_pertandingan'),
    path('form-peminjaman-stadium/', show_form_peminjaman_stadium, name='form_peminjaman_stadium'),
]