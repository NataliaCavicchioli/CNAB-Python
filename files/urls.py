from django.urls import path
# from django import views
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path('files/', views.upload, name='upload'),
   path('files/view/', views.view, name='view'),

]


# For example, we can use the name parameter to 
# link to our home page from any other page by adding the following link in a template:
# <a href="{% url 'index' %}">Home</a>.   
