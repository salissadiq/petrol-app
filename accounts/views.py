from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import SalesForm
# Create your views here.



def home(request):
    sales = Sales.objects.all()
    users = User.objects.all()
    total_users = users.count()
    total_sales = sales.count()
    context = {'sales': sales, 'users': users, 'total_users': total_users, 'total_sales': total_sales}
    return render(request, 'accounts/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def user(request, pk):
    user = User.objects.get(id=pk)
    sales = user.sales_set.all()
    total_sales = sales.count()
    context = {'user': user, 'sales': sales, 'total_sales': total_sales}
    return render(request, 'accounts/user.html', context)

def createSale(request, pk):
	user = User.objects.get(id=pk)
	form = SalesForm(initial = {'user': user})
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'accounts/sale_form.html', context)

def updateSale(request, pk):

	sale = Sales.objects.get(id=pk)
	form = SalesForm(instance = sale)

	if request.method == 'POST':
		form = SalesForm(request.POST, instance=sale)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/sale_form.html', context)

def deleteSale(request, pk):
	sale = Sales.objects.get(id=pk)
	if request.method == "POST":
		sale.delete()
		return redirect('/')

	context = {'item':sale}
	return render(request, 'accounts/delete_sale.html', context)
