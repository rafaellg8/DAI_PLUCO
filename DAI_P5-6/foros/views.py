#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.template import RequestContext
from plucoApp.models import Comment,Forum,User
from django.http import HttpResponse
from plucoApp.forms import Forums,Comments,userForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime

@login_required
def showComments(request,theme):
    #obtenemos el foro asociado a un tema
    form = Forum.objects.get(theme=theme)
    #filtramos comentarios de un foro con un tema
    comForm = Comment.objects.filter(theme=form).order_by('date')

    if request.method =="POST":
        idC = 0
        com = Comment.objects.order_by('idComment')[:1]
        for c in com:
            idC = c.idComment+1

        com = Comments(request.POST)

        username = request.user
        f = get_object_or_404(Forum,theme=theme)
        #validamos el formulario
        if com.is_valid():
            comment = Comment()
            comment.theme = f
            comment.idComment = idC
            comment.username = username
            comment.commentText = request.POST["commentText"]
            comment.title = request.POST["title"]
            comment.date = datetime.date.today()

            comment.save()

            return redirect("/foros/theme/"+theme,{'com': comForm,})
    else:
        com = Comment.objects.order_by('idComment')[:1]
        for c in com:
            idC = c.idComment+1
        com = Comment()

    context = {'com': comForm,'commentForm':com,'theme': theme}
    return render(request,'comentarios.html',context)

@login_required
def showForums(request):
    com = Forum.objects.all()
    context = {'forum': com}

    if request.method =="POST":
        form = Forums(request.POST)
        #validamos el formulario
        if form.is_valid():
            newForum = Forum()
            newForum.title = request.POST["title"]
            newForum.theme = request.POST["theme"]
            newForum.asignature = request.POST["asignature"]
            newForum.save()

            return redirect("/foros")
        else:
            print form.errors
    else:
        form = Forum()
    return render(request,'foros.html', {'forum': com,'form': form})

@login_required
def comment(request,theme):
    if request.method =="POST":
        com = Comment.objects.order_by('idComment')[:1]
        for c in com:
            idC = c.idComment+1

        com = Comments(request.POST)

        username = request.user
        f = get_object_or_404(Forum,theme=theme)
        #validamos el formulario
        if com.is_valid():
            comment = Comment()
            comment.theme = f
            comment.idComment = idC
            comment.username = username
            comment.commentText = request.POST["commentText"]
            comment.title = request.POST["title"]
            comment.date = datetime.date.today()

            comment.save()

            return (showComments(request,theme))
        else:
            print comm.errors
    else:
        com = Comment.objects.order_by('idComment')[:1]
        for c in com:
            idC = c.idComment+1
        com = Comment()

    return render(request,'comentarios.html',{'commentForm':com})


@login_required
def like_comment(request):
    context = RequestContext(request)
    cat_id = None

    if request.method == 'GET':
        cat_id = request.GET.get('idComment','')
        #No encuentra la categoria
    likes = 0
    if cat_id:
        category = Comment.objects.get(id=int(cat_id))
        if category:
            likes = category.likes + 1
            category.likes =  likes
            category.save()

    return HttpResponse(likes)


@login_required
def forums(request):
    if request.method =="POST":
        form = Forums(request.POST)
        #validamos el formulario
        if form.is_valid():
            newForum = Forum(request.POST["title"],request.POST["theme"],request.POST["asignature"])
            return render(request,'foros.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = Forum()
    return render(request,'foros.html', {'form': form},)

@login_required
def theme(request,theme):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        form = Forum.objects.get(theme=theme)
        context_dict['forum_name'] = form.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        comm = Comment.objects.filter(theme=form)

        # Adds our results list to the template context under name pages.
        context_dict['comm'] = comm
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['theme'] = form
    except Forum.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'forosCat.html', context_dict)
