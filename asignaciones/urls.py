from django.urls import path
from . import views
urlpatterns = [
    path('asignacion',views.asignacion,name= "asignacion")
]
