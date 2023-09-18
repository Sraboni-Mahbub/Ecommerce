from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *



# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info('Username or password wrong')
    return render(request, 'ecom/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created')
            return redirect('login')
    context = {'form':form}
    return render(request, 'ecom/register.html', context)


@login_required
def home(request):
    return render(request, 'ecom/home.html')

