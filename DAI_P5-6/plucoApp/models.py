#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
      title = models.CharField(max_length=128,help_text="Título de la hebra o foro nuevo",unique=True)
      theme = models.CharField(max_length=50,help_text="Tema",unique=True)
      asignature = models.CharField(max_length=25,help_text="asignature",unique=True)

      def __unicode__(self):
            return self.title

class UserProfile(models.Model):
     # Usa una instancia de User de contrib auth models
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    address = models.TextField(max_length=50,help_text="dirección postal")
    picture = models.ImageField(upload_to='media', blank=True)

    # Return the user, for a request.user
    def getUser():
        return self

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Comment(models.Model):
      """docstring for Comment"""
      """temas, idComentario (número comentario)
      título, comentario, usuario que hace el comentario,
      url donde el usuario pone la url de su archivo a compartir si procede"""
      theme = models.ForeignKey(Forum)
      idComment = models.IntegerField(null=False)
      title = models.CharField(max_length=128,help_text="Título del comentario, asunto",unique=True)
      commentText = models.TextField(max_length=500,help_text="Introduce aquí tu comentario")
      username = models.ForeignKey(User)
      date = models.DateField()
      #url = models.URLField(blank=True)

      def __unicode__(self):
            return self.title
