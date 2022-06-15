
from email.mime import message
from os import name
from urllib import response
from django.contrib import messages
from django.urls import reverse
from .models import Produkty

from telnetlib import AUTHENTICATION
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from pkg_resources import require
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .forms import UzytkownikRejestracjaForm
from .forms import LogowanieForm 
from .forms import Profil
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from.models import *

def produkt1(request):
    return render(request, 'Ap/1.html')

def index(request):
     
    return render(request, 'Ap/index.html')

def baza(request):
         
    return render(request, 'Ap/baza.html')

def tworzywa(request):

    return render (request, 'Ap/tworzywa_sztuczne.html')

def metal(request):
    
    return render(request, 'Ap/metal.html')
def dane(request):
        
    return render(request, 'Ap/dane.html')

def kontakt(request):
    
    return render(request, 'Ap/kontakt.html')
    
def koszyk(request):
    return render(request, 'Ap/koszyk.html')




def rejestracja(request):
    if request.method == 'POST':
        form = UzytkownikRejestracjaForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
           
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
        
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
          
            return redirect('index')
    else:
        form = UzytkownikRejestracjaForm()
    return render(request, 'Ap/rejestracja.html', {'form': form})


def logowanie(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'Ap/index.html', {'username': username})
            
        else:
            messages.error(request, "złe dane")
            return redirect('logowanie')
    
    return render(request, "Ap/logowanie.html")


# def produkty(request):
#     produkty=Produkty.objects.all().filter().order_by('nazwa')
#     return render(request,"Ap/produkty.html",context={'produkty':produkty})

#     if request.method=='POST':
#         form=LogowanieForm(request.POST or None)
#         #if form.is_valid():
#           #  cd=form.cleaned_data
#         user=authenticate(email='email',passwordx='passwordx')
         
#         if user is not None:
#             #if user.is_active:
#                 login(request, user)
#                 return redirect('baza.html')  
#         else:
#             messages.error(request,'Nieprawidlowe dane')
#             return redirect('index')
#     else:
 
#         form=LogowanieForm()
#         return render(request,'baza.html')  
        
#     return render (request=request,template_name='Ap/logowanie.html',context={'form':form})

def WidokProfilu(request):

    if request.method=="POST":
        form=ProfilForm(request.POST)
        if form.is_valid():
            #form=Profil(user=request.user,name=request.POST['name'],surname=request.POST['surname'])
            form.save()
            messages.success(request, 'Czesc, Uaktualnij swoj profil {reguest.user.username} !!')
    else:

        form=ProfilForm()
    form=Profil.objects.all()
    context={'form': form}
    return render(request,"Ap/profil.html",context )
        

        
    context ={}
    context['profil']= Profil()
    return render(request, "Ap/profil.html", context)
    

            
def wszystkieProdukty(request):
    context = { 'produkty' : Produkty.objects.all() }
    return render (request, "Ap/produkty.html", context)


def add_to_cart(request, **kwargs):

    user_profile = get_object_or_404(Klient, user=request.user)
  
    produkt = Produkty.objects.filter(id=kwargs.get('id', "")).first()
 
    if produkt in request.user.objects.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list')) 
   
    order_item, status = OrderItem.objects.get_or_create(produkt = produkt)
  
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:

        user_order.save()

   
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))



