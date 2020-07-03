from django.shortcuts import render, redirect

# Create your views here.
from django.core.files.storage import default_storage

from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm 
from .form import CreateUserForm
from django.contrib import messages


def home(request):
	order = Order.objects.all()
	customer  = Customer.objects.all()
	context = {'order':order, 'customer':customer}

	return render(request,'customer/home.html',context)



def product(request):
	products  = Product.objects.all()
	return render(request,'customer/product.html', {'products': products})




def customer_view(request):
	customer_list  = Customer.objects.all()
	return render(request,'customer/customer.html',{'customer_list': customer_list})



def login_form(request):
	return render(request,'customer/login.html')




def request_form(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form_cleaned_data.get('username')
			messages.success(request,'Account created successfully for '+user)
			return redirect('http://127.0.0.1:8000/customer/login/')
			
	context = {'form' : form}
	return render(request,'customer/request.html',context)
