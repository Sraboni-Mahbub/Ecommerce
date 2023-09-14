from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import *
from .forms import *



# Create your views here.

def home(request):
    return render(request, 'ecom/home.html')

def login(request):
    return render(request, 'ecom/login.html')

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'ecom/register.html', context)

