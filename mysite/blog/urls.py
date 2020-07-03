from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('images/', views.image_view, name='images'),
    path('article/', views.article_view, name='article'),
 	path('register/', views.register_form, name='register'),
	path('profile/', views.profile_view, name='profile'),
	path('travel_diaries/', views.travel_diaries, name='travel_diaries'),
 	path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
 	path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),	
 ]


 