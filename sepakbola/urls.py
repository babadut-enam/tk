from sepakbola.views import show_home, register, login_user, logout_user
from sepakbola.views import show_peminjaman_stadium, show_dashboard, show_form_peminjaman_stadium, show_mengelola_tim
from sepakbola.views import show_manage_pertandingan, show_peristiwa_tim, show_pembuatan_pertandingan, show_form_pemilihan_jadwal, show_form_pembuatan_pertandingan
from sepakbola.views import register_manajer_penonton, register_panitia, show_list_pertandingan
from sepakbola.views import show_history_rapat, show_pilih_pelatih, show_pilih_pemain
from sepakbola.views import show_history_rapat, show_dashboard_manajer, show_list_waktu_stadium_sketch
from sepakbola.views import form_isi_rapat, mulai_rapat, mulai_pertandingan, tim1_peristiwa, tim2_peristiwa
from sepakbola.views import pembelian_tiket, pembelian_tiket2, pembelian_tiket3, pembelian_tiket4
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
    path('waktu-stadium/', show_list_waktu_stadium_sketch, name='waktu-stadium'),
    path('form-peminjaman-stadium/', show_form_peminjaman_stadium, name='form-peminjaman-stadium'),
    path('list-pertandingan/', show_list_pertandingan, name='list-pertandingan'),
    path('history-rapat/', show_history_rapat, name='history-rapat'),
    path('manage-pertandingan/', show_manage_pertandingan, name='manage-pertandingan'),
    path('pembuatan-pertandingan/', show_pembuatan_pertandingan, name='pembuatan-pertandingan'),
    path('manage-pertandingan/peristiwa-tim/', show_peristiwa_tim, name='peristiwa-tim'),
    # path('manage-pertandingan/peristiwa-tim/<uuid:id>/', show_manage_pertandingan, name='peristiwa-tim'), TODO: ini yang bener tapi belum ada data jadi pake yang atas
    path('pembuatan-pertandingan/form-pemilihan-jadwal/', show_form_pemilihan_jadwal, name='form-pemilihan-jadwal'),
    path('pembuatan-pertandingan/form-pembuatan-pertandingan/', show_form_pembuatan_pertandingan, name='form-pembuatan-pertandingan'),
    path('form-isi-rapat/', form_isi_rapat, name='form_isi_rapat'),
    path('mulai-rapat/', mulai_rapat, name='mulai_rapat'),
    path('mulai-pertandingan/', mulai_pertandingan, name='mulai_pertandingan'),
    path('tim1-peristiwa/', tim1_peristiwa, name='tim1_peristiwa'),
    path('tim2-peristiwa/', tim2_peristiwa, name='tim2_peristiwa'),
    path('pembelian-tiket-stadium/', pembelian_tiket, name='pembelian_tiket'),
    path('pembelian-tiket-waktu/', pembelian_tiket2, name='pembelian_tiket2'),
    path('pembelian-tiket-vs/', pembelian_tiket3, name='pembelian_tiket3'),
    path('pembelian-tiket-checkout/', pembelian_tiket4, name='pembelian_tiket4'),

]