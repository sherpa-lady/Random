from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *


from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .form import CreateUserForm
from django.contrib import messages


@login_required
def profile_view(request):
	return render(request,'blog/profile.html')



def login_form(request):
	return render(request,'blog/login.html')




def register_form(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,f'Ready to login !')
			return redirect('login')
	else:
		form = CreateUserForm()
	context = {'form' : form}
	return render(request,'blog/register.html',context)



def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    data = Article.objects.all()
    return render(request,"index.html",{'data':data})





def index(request):
	article = Article.objects.all()
#	context = { 'article':article}
#	render(request,'base.html',{'article': article})
	return render(request,'blog/index_page.html',{'article': article})




def image_view(request):
	images = Article.objects.all()
	return render(request,'blog/images.html', {'images': images})




def article_view(request):
	file = Article.objects.all()
	return render(request,'blog/article.html',{'file': file})

def travel_diaries(request):
	context = Article.objects.filter(category = 'Travel diaries')
	return render(request,'blog/travel_diaries.html',{'context':context})
