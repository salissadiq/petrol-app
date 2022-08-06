from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.



def home(request):
    sales = Sales.objects.all()
    users = User.objects.all()
    context = {'salses': sales, 'users': users}
    return render(request, 'accounts/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')
