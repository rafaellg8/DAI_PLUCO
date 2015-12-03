#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pluco.settings')

import django
django.setup()

from plucoApp.models import Forum,User,Comment

#aquí generamos las tablas con los datos insertados
def test():
      forum = addForum('Ayuda','Tema de Ayuda','HELP')

      testingUser = addUser('testingUser','Testing','Testing firstname',
            'Testing SecondName','0001-01-01','testing@mail.com','password')

      #añadimos ahora el testing user y el forum como una clave externa a comentarios
      addComment(forum,1,'Testeando','Testeando un comentario',testingUser,'http://urlnube/recurso',datetime.date.today())

      for f in Forum.objects.all():
            for c in Comment.objects.all():
                  print "- {0} - {1}".format(str(f), str(c))

def addForum(theme,title,asignature):
            forum = Forum.objects.get_or_create(title=title,theme=theme,asignature=asignature)[0]
            forum.save()
            return forum

def addUser(userName,name,firstName,secondName,birthday,email,password):
      u = User.objects.get_or_create(userName=userName,name=name,firstName=firstName,
            secondName=secondName,birthday=birthday,email=email,password=password)[0]
      return u

def addComment(forum,idC,tit,commentTxt,user,url,date):
      com = Comment.objects.get_or_create(theme=forum,idComment=idC,title=tit,commentText=commentTxt,userName=user,url=url,date=date)[0]
      return com

if __name__ == '__main__':
      print "Starting Testing..."
      test()
