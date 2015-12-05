#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pluco.settings')

import django
django.setup()

from plucoApp.models import Forum,User,Comment
from django import forms

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userName','name','email','password','address')


    def addUser(userName,name,email,password,address):
          u = User.objects.get_or_create(userName=userName,name=name,email=email,password=password,address=address)[0]
          u.save()
          return u

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('theme','title','commentText','url',)

    def addComment(forum,idC,tit,commentTxt,user,url,date):
          com = Comment.objects.get_or_create(theme=forum,idComment=idC,title=tit,commentText=commentTxt,userName=user,url=url,date=date)[0]
          com.save()
          return com

class Forums(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title','theme','asignature',)

    def addForum(self,title,theme,asignature):
                forum = Forum.objects.get_or_create(title=title,theme=theme,asignature=asignature)[0]
                forum.save()
                print ("Guardamos el foro")
                return forum
