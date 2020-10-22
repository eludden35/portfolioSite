from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.regTR),
    path('newU', views.newUser),
    path('login', views.logN),
    path('bootPrac', views.boot)
]
