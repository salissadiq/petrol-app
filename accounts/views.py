from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import SalesForm, CreateUserForm
# Create your views here.


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			
		context = {'form': form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    sales = Sales.objects.all()
    users = User.objects.all()
    total_users = users.count()
    total_sales = sales.count()
    context = {'sales': sales, 'users': users, 'total_users': total_users, 'total_sales': total_sales}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url='login')
def user(request, pk):
    user = User.objects.get(id=pk)
    sales = user.sales_set.all()
    total_sales = sales.count()
    context = {'user': user, 'sales': sales, 'total_sales': total_sales}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteSale(request, pk):
	sale = Sales.objects.get(id=pk)
	if request.method == "POST":
		sale.delete()
		return redirect('/')

	context = {'item':sale}
	return render(request, 'accounts/delete_sale.html', context)
