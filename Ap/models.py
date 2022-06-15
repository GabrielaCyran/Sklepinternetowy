from binascii import rledecode_hqx
from ctypes import addressof
from distutils.command.upload import upload
from email.errors import MessageError
from tabnanny import verbose
from tkinter import CASCADE, Place, Widget
from turtle import up
from urllib.request import CacheFTPHandler
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.forms import BooleanField, CharField, ImageField
from django.conf import settings
#from one.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User

class Profil(models.Model):
    Kobieta = 'K'
    Meżczyzna = 'M'
   
    Pleć = (
        (Kobieta, 'Kobieta'),
        (Meżczyzna, 'Mezczyzna'),
       
    )
    
    user=models.ForeignKey(User,blank=False,on_delete=models.CASCADE,)
    name=models.CharField(max_length=100,blank=False)
    surname=models.CharField(max_length=100,blank=False)
    gender=models.BooleanField(choices=Pleć)
    birthday=models.DateField(blank=True, null=True)
    role=models.CharField(max_length=100)
    #zdjecie=models.ImageField(upload_to='static/',blank=True)

    def __str__(self) :
        return self.user
    

    class Meta:
   
        verbose_name_plural='profile'

class Klient(models.Model):
    imie=models.CharField(max_length=50)
    nazwisko=models.CharField(max_length=70)
    adres=models.CharField(max_length=100)
    telefon=models.CharField(max_length=16)
    class Meta:
       
        verbose_name_plural='klienci'

   
class Kategoria(models.Model):
    nazwa=models.CharField(max_length=100)
    opis=models.TextField(max_length=1000,null=False,blank=True)
    def _str_(self):
        return self.nazwa
    class Meta:
       
        verbose_name_plural='kategorie'

class Produkty(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    nazwa=models.CharField(max_length=100,blank=True,unique=True)
    opis=models.TextField(max_length=300, null=True, blank=True)
    cena=models.DecimalField(max_digits=10,decimal_places=2)
    zdjecie=models.ImageField(upload_to='static',default='')
    slug=models.SlugField(max_length=50,unique=True, blank=True)
    zasob=models.IntegerField()
    dostepnosc=models.BooleanField(default=True)
    kategoria=models.ForeignKey(Kategoria,on_delete=models.CASCADE)
    nowy_produkt=models.DateTimeField('dodano produkt',auto_now_add=True)
    def  __str__(self) :
         return self.nazwa
    class Meta:
           
        verbose_name_plural='produkty'

class OrderItem(models.Model):
    produkt = models.OneToOneField(Produkty, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.produkt.name


#def get_staus(self, new_status: int)-> None:
        #self.status= new_status
class Platnosc(models.Model):
    zamowienie_id=models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    forma_platnosci=models.CharField(max_length=1000)
    class Meta:
           
        verbose_name_plural='platnosci'





class Koszyk(models.Model):
    nazwa=models.ForeignKey(Produkty,on_delete=models.CASCADE)
    ilosc=models.IntegerField()
    cena=models.DecimalField(max_digits=10,decimal_places=2)
    rabat=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
           
        verbose_name_plural='koszyk'

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Klient, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.produkt.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)




