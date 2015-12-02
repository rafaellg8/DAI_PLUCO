from django.shortcuts import render
from django.views.generic import ListView
from models import Comment,Forum,User
from django.http import HttpResponse
from plucoApp.forms import Forum

def comment(request):
    return render(request,'comentarios.html')

def forums(request):
    form = Forum
    return render(request,'foros.html', {'form': form})
