from django.db import models
from django import forms
import datetime

class Article(models.Model):	
    CATEGORY =(
		('Travel diaries','Travel diaries'),
		('Achievement','Achievement', ),
		('college','college'),
		('others','others'),
		  )
    title = models.CharField(max_length = 200)
    article = models.TextField(max_length = 600, null=True, blank=True)
    file = models.FileField(null = True, blank = True)
    images =models.ImageField(null = True, blank = True)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    category = models.CharField(max_length=200, choices = CATEGORY,null = True)
    date_created =models.DateTimeField(auto_now_add=True,blank = True, null = True)


    def __str__(self):
    	return self.title


class UploadFileForm(forms.Form):	
    title = forms.CharField(max_length=50)
    file = forms.FileField()


