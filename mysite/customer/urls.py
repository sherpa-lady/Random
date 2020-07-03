from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.home, name='index'),
    path('product/', views.product, name='product'),
    path('customer_view/', views.customer_view, name='customer'),
    path('upload/', views.upload, name='upload'),
	path('login/', views.login_form, name='login'),
    path('request/', views.request_form, name='request'),


]
