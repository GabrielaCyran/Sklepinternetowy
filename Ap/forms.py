from calendar import c
import email
from math import prod
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Produkty
from .models import Profil
from .models import Kategoria




class UzytkownikRejestracjaForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        
class LogowanieForm(forms.Form):
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput)



class ProfilForm(forms.ModelForm):
  
    class Meta:
        model=Profil
        fields='__all__'#('name','surname','gender','birthday','zdjecie')       
class KategorieForm(forms.ModelForm):
      
    class Meta:
        model=Kategoria
        fields='__all__'


