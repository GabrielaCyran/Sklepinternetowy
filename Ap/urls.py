from django.urls import URLPattern, path


from .import views 


urlpatterns= [
path('rejestracja/',views.rejestracja,name="rejestracja"),
path('', views.index, name="index"),
path ('logowanie/',views.logowanie,name="logowanie"),
path('index/',views.index,name="index"),
path('baza/', views.baza,name="baza"),
path('produkty/', views.wszystkieProdukty,name="produkty"),
path('profil/', views.WidokProfilu,name="profil"),
path('tworzywa_sztuczne/', views.tworzywa,name="tworzywa_sztuczne"),
path('metal/', views.metal,name="metal"),
path('produkty/<int:produkt_id>/', views.koszyk, name='koszyk'),
path('add-to-cart/<int:item_id>', views.add_to_cart, name="add_to_cart"),
path('koszyk/', views.koszyk, name="koszyk"),
path('dane/', views.dane, name="dane"),
path('kontakt/', views.kontakt, name="kontakt")
]

