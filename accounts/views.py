from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
    #En la funcion register creamos un objeto form basado en 
    # el RegistrationForm(), desemos que se diriga hacia el template html
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        #valor =0
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            dpi = form.cleaned_data['dpi']
            fecha_de_nacimiento = form.cleaned_data['fecha_de_nacimiento']
            password = form.cleaned_data['password']
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number = phone_number
            user.dpi=dpi
            user.fecha_de_nacimiento = fecha_de_nacimiento
            user.save()
            messages.success(request,'Se registro el usuario exitosamente')
            return redirect('register')
            #valor =1
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html',context)


def eleccion_usuario(request):
    return render(request, 'accounts/Registro.html')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Home')
        else:
            messages.error(request,'Las credenciales son incorrectas')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'Has salido de sesion')
    return redirect('login')    