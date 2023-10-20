from django.urls import path
from . import views

urlpatterns = [
    path('cursos', views.Cursos, name = "Cursos"),
]

