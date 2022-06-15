
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profil, Klient, Kategoria, Produkty, Platnosc

# #class AdminUser(UserAdmin):
#     list_display=('email','name','surname','username','last_login','last_activate')
#     list_display_links=('email','name','surname')
#     readonly_filds=('last_login')

# class ProduktAdmin(admin.ModelAdmin):
#     list_display=('nazwa','cena','zasób','kategoria','dostepnosc')
#     prepopulated_fields={'slug':('nazwa')}
#admin.site.register(User,AdminUser)
#admin.site.register(Useer)
#admin.site.register(MyUser)
#admin.site.register(Produkty)
admin.site.register(Profil)
admin.site.register(Klient)
admin.site.register(Kategoria)
admin.site.register(Produkty)
admin.site.register(Platnosc)

