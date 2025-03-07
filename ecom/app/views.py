from django.shortcuts import render, redirect
from.models import UserProfile,Order,Delivery,Product,Brand
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_phone= request.POST['email']
        password = request.POST['password']
        try:
            user = UserProfile.objects.get(email=email_phone, password=password)
            if check_password(password, user.password):
                auth_login(request, user) # Note: Use a different name for your view function
                return redirect('home')
            else:
                return render(request, 'login.html',{'error': 'Invalid password'})
        except UserProfile.DoesNotExist:
            return render(request, 'login.html', {'error': 'Email does not exist'})
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password (password)
        user = UserProfile (full_name=username,email=email, password=hashed_password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')

def home_view(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def cart(request):
    return render(request, 'cart.html')

def Toys(request):
    return render(request, 'Toys.html')

def Kids_ts(request):
    return render(request, 'Kids_ts.html')

def Shirts(request):
    return render(request, 'Shirts.html')

def Trousers(request):
    return render(request, 'Trousers.html')

def Shoes(request):
    return render(request, 'Shoes.html')

def School_Bags(request):
    return render(request, 'School_Bags.html')

def Women_Dresses(request):
    return render(request, 'Women_Dresses.html')

def WomenHandbags(request):
    return render(request, 'WomenHandbags.html')

def WomenJewelry(request):
    return render(request, 'WomenJewelry.html')

def billingpage(request):
    return render(request, 'billingpage.html')

def makeup(request):
    return render(request, 'makeup.html')


def skincare(request):
    return render(request, 'skincare.html')


def haircare(request):
    return render(request, 'haircare.html')

def smartphone(request):
    return render(request, 'smartphone.html')

def laptop(request):
    return render(request, 'laptop.html')

def headphone_charger(request):
    return render(request, 'headphone_charger.html')

