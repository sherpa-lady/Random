from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


class Customer(models.Model):
	user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length = 300)
	email = models.EmailField(max_length = 200,null = True)
	profile_pic = models.ImageField(null = True,blank = True)
	time = models.DateTimeField(auto_now_add = True , null = True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name




class Product(models.Model):
	CATEGORY =(
			('pending','pending'),
			('Out of delivery','Out of delivery', ),
			('delivered','delivered'),
		)
	name = models.CharField(max_length=200)
	price = models.FloatField(max_length=200)
	category = models.CharField(max_length=200, choices = CATEGORY )
	description = models.TextField(max_length=200, null = True)
	date_created =models.DateTimeField(auto_now_add=True)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name





class Order(models.Model):
	STATUS =(
			('pending','pending'),
			('Out of delivery','Out of delivery', ),
			('delivered','delivered'),
		)
	customer = models.ForeignKey(Customer, null = True,on_delete = models.SET_NULL)
	product = models.ForeignKey(Product, null = True,on_delete = models.SET_NULL)
	date_created =models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=200, choices = STATUS )



def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name,uploaded_file)
		print(uploaded_file.name)
		print(uploaded_file.size)
	return render(request,'customer/upload.html')

