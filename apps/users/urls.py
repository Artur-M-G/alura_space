from django.urls import path
from .views import login, singup, logout

urlpatterns = [
    path('login', login, name='login'),
    path('singup', singup, name='singup'),
    path('logout', logout, name='logout'),
]
