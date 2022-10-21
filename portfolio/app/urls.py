from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('contact_me', views.contact_me, name='contact_me'),
    path('about_me', views.about_me, name='about_me'),
]