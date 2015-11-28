#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Forum(models.Model):
      title = models.CharField(max_length=128,unique=True)
      theme = models.CharField(max_length=50,unique=True)
      asignature = models.CharField(max_length=25,unique=True)

      def __unicode__(self):
            return self.title

class User(models.Model):
      userName = models.CharField(max_length=25,unique=True)
      name = models.CharField(max_length=25)
      firstName = models.CharField(max_length=25)
      secondName = models.CharField(max_length=25)
      birthday = models.DateField()
      email = models.EmailField()
      password = models.CharField(max_length=25)

      def __unicode__(self):
            return self.userName

class Comment(models.Model):
      """docstring for Comment"""
      """temas, idComentario (número comentario)
      título, comentario, usuario que hace el comentario,
      url donde el usuario pone la url de su archivo a compartir si procede"""
      theme = models.ForeignKey(Forum)
      idComment = models.IntegerField(null=False)
      title = models.CharField(max_length=128,unique=True)
      commentText = models.CharField(max_length=500)
      userName = models.ForeignKey(User)
      url = models.URLField()

      def __unicode__(self):
            return self.title
