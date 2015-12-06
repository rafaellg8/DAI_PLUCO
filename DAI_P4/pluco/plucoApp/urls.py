from django.conf.urls import patterns, url
from plucoApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'about',views.about,name='about'),
        url(r'contact',views.contact,name='contact'),
        url(r'register',views.register,name='register'),
        url(r'^login/$',views.user_login,name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^perfil/$',views.user_profile,name='perfil')
        )
