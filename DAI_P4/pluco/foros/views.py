from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext
from plucoApp.models import Comment,Forum,User
from django.http import HttpResponse
from plucoApp.forms import Forums,Comments,UserForms
from django.shortcuts import redirect
import datetime

def showComments(request):
    com = Comment.objects.all()
    context = {'com': com}
    #render
    return render(request,'comentarios.html',context)

def comment(request):
    if request.method =="POST":
        com = Comments(request.POST)
        #validamos el formulario
        if com.is_valid():
            newComment = Comment(request.POST["theme"],request.POST["idComment"],request.POST["title"],request.POST["commentText"],request.POST["userName"],request.POST["url"],datetime.date.today)
            return redirect('foros.views.details',pk=com.pk)
    else:
        com = Comment()
    return render(request,'comentarios.html',{'commentForm':com},context_instance=RequestContext(request))

def forums(request):
    if request.method =="POST":
        form = Forums(request.POST)
        #validamos el formulario
        if form.is_valid():
            newForum = Forum(request.POST["title"],request.POST["theme"],request.POST["asignature"])
            return redirect('foros.views.details',pk=form.pk)
    else:
        form = Forum()
    return render(request,'foros.html', {'form': form},context_instance=RequestContext(request))
