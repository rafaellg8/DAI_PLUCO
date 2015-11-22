from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'hijo.html')
def login(request):
      return render(request,'login.html')
def register(request):
      return render(request,'register.html')
def about(request):
      return render(request,'about.html')      
def contact(request):
      return render(request,'contact.html')      