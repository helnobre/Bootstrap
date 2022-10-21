import email
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Info

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact_me(request):
    if(request.method == "POST"):
        name = request.POST['name'],
        email = request.POST['email'],
        content = request.POST['content']
        instance = Info(nome=name ,e_mail= email, content= content)
        instance.save()
        

    return render(request, 'contact_me.html')

def about_me(request):
    return render(request, 'about_me.html')
