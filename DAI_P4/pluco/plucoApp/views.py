from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'hijo.html')
def login(request):
      return render(request,'/home/rafaellg8/Documentos/GII/Cuarto/DAI/DAI_PLUCO/DAI_P4/pluco/plucoApp/templates/login.html')
def register(request):
      return render(request,'/home/rafaellg8/Documentos/GII/Cuarto/DAI/DAI_PLUCO/DAI_P4/pluco/plucoApp/templates/register.html')
def about(request):
      return render(request,'/home/rafaellg8/Documentos/GII/Cuarto/DAI/DAI_PLUCO/DAI_P4/pluco/plucoApp/templates/about.html')      
def contact(request):
      return render(request,'/home/rafaellg8/Documentos/GII/Cuarto/DAI/DAI_PLUCO/DAI_P4/pluco/plucoApp/templates/contact.html')      