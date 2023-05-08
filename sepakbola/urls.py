from sepakbola.views import show_home, register, login_user, logout_user
from sepakbola.views import show_peminjaman_stadium, show_dashboard, show_form_peminjaman_stadium, show_mengelola_tim, show_manage_pertandingan
from sepakbola.views import register_manajer_penonton, register_panitia, show_list_pertandingan
from sepakbola.views import show_history_rapat, show_pilih_pelatih, show_pilih_pemain
from sepakbola.views import show_history_rapat, show_dashboard_manajer
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
    path('dashboard-manajer/', show_dashboard_manajer, name='dashboard-manajer'),
    path('mengelola-tim/', show_mengelola_tim, name='mengelola-tim'),
    path('pilih-pemain/', show_pilih_pemain, name='pilih-pemain'),
    path('pilih-pelatih/', show_pilih_pelatih, name='pilih-pelatih'),
    path('peminjaman-stadium/', show_peminjaman_stadium, name='peminjaman-stadium'),
    path('form-peminjaman-stadium/', show_form_peminjaman_stadium, name='form-peminjaman-stadium'),
    path('list-pertandingan/', show_list_pertandingan, name='list-pertandingan'),
    path('history-rapat/', show_history_rapat, name='history-rapat'),
]