from django.conf.urls import patterns, url
from plucoApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'register',views.register,name='register'),
        url(r'about',views.about,name='about'),
        url(r'contact',views.contact,name='contact'),
        url(r'login',views.login,name='login'),
        )
