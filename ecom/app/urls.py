from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('', views.home_view, name='home'),
    path('search/', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('Toys/', views.Toys, name="Toys"),    
    path('Kids_ts/', views.Kids_ts, name="Kids_ts"),    
    path('Shirts/', views.Shirts, name="Shirts"),    
    path('Shoes/', views.Shoes, name="Shoes"),    
    path('Trousers/', views.Trousers, name="Trousers"),    
    path('School_Bags/', views.School_Bags, name="School_Bags"),    
    path('Women_Dresses/', views.Women_Dresses, name="Women_Dresses"),    
    path('WomenHandbags/', views.WomenHandbags, name="WomenHandbags"),    
    path('WomenJewelry/', views.WomenJewelry, name="WomenJewelry"),    
    path('billingpage/', views.billingpage, name="billingpage"), 
    path('makeup/', views.makeup, name="makeup"), 
    path('skincare/', views.skincare, name="skincare"), 
    path('haircare/', views.haircare, name="haircare"), 
    path('smartphone/', views.smartphone, name="smartphone"), 
    path('laptop/', views.laptop, name="laptop"), 
    path('headphone_charger/', views.headphone_charger, name="headphone_charger"), 
]

