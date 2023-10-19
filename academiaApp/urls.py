from django.urls import path
from academiaApp import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('login', views.login, name = "Login"),
]