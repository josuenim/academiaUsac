from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'home.html') #Renderizar plantillas.
def contacto(request):
    return render(request,'contacto.html')






