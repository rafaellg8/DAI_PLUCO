##Practica 4 Tango , Rango with Django

##Algunos comandos
###Crear proyecto
```
django-admin.py startproject pluco
```
###Run y migrate
```
python pluco/manage.py migrate

python pluco/manage.py runserver
```

###Crear una app
**Dentro del directorio**
```
python manage.py startapp plucoApp
```

###Añadimos la app dentro del directorio pluco, en el archivo settings.py
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'plucoApp',
)
```

###Creamos la vista, que recoge las peticiones y respuestas al cliente
**view.py**
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")
```

###Creamos el mapeo de urls dentro de la app, ulrs.py
```
from django.conf.urls import patterns, url
from plucoApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
```

###Configuramos el mapeo final dentro del proyecto, en el archivo pluco/urls.py
```
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^plucoApp/', include('plucoApp.urls')), # ADD THIS NEW TUPLE!
)
```