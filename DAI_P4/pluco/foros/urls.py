from django.conf.urls import patterns
from django.conf.urls import url

from foros import views

urlpatterns = patterns('',
    url(r'comentario', views.comment, name='comment'),
    url(r'^$', views.forums, name='forums'),
)
