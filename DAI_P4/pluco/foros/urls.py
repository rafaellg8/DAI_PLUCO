from django.conf.urls import patterns
from django.conf.urls import url

from foros import views

urlpatterns = patterns('',
    url(r'(?P<theme>[\w\-]+)/$', views.showComments, name='theme'),
    url(r'(?P<theme>[\w\-]+)/nuevoComentario', views.comment, name='comment'),
    url(r'^$', views.showForums, name='forums'),
    url(r'foros', views.showForums, name='comment'),
)
