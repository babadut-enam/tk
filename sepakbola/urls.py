from sepakbola.views import show_home, register, login_user, logout_user
from sepakbola.views import show_peminjaman_stadium, show_dashboard
from django.urls import path

app_name = 'sepakbola'

urlpatterns = [
    path('', show_home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('peminjaman-stadium/', show_peminjaman_stadium, name='peminjaman_stadium'),
]