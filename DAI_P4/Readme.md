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

###Configuramos los templates y los URL en el archivo settings, configuramos el path de los directorio
```
print BASE_DIR

BASE_DIR_FILES = BASE_DIR+'/pluco/'

print BASE_DIR_FILES

TEMPLATE_PATH = BASE_DIR_FILES+'templates/'

print TEMPLATE_PATH

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR_FILES, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

###Configuramos el directorio static donde van las imagenes y los css
Archivo settings.py
```
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = ('STATIC_PATH',)
```

Y en el directorio raíz del proyecto guardamos la carpeta static. Ahora configuramos en cada archvio donde tengamos css o imágenes:
index.html:
```
img src="{% static "images/foros.jpg" %}" width="300px" height="185px
```

##Modelos SQL
Para los modelos definimos las clases con cada modelo en **models.py**. Tendremos 2 clases por ahora, **FOROS** y **COMENTARIOS**, donde cada FORO tiene uno o varios COMENTARIOS asociados.

[enlace a models.py](/plucoApp/models.py)

Sincronizamos ahora la base de datos para que nos cree las tablas y demás:
```
python manage.py syncdb
```

Ahora hacemos la migración y creamos un nuevo superuser:
```
python manage.py makemigrations
```

Generamos las migraciones:
```
python manage.py migrate
```

Si todo da OK, generamos el superuser:
```
 python manage.py createsuperuser
 ```

###Configuramos Interfaz Usuario
Para ello debemos editar el archivo admin.py
```
from django.contrib import admin
from plucoApp.models import Comment,Forum,User
#importamos de plucoApp los modelos
# Register your models here.

admin.site.register(Comment)
admin.site.register(Forum)
admin.site.register(User)
```
Volvemos a hacer las migraciones y ejecutamos el servidor.
```
python manage.py makemigrations plucoApp
```
```
 python manage.py migrate plucoApp
 ```
```
python manage.py runserver
```
Ahora si abrimos en el navegador **localhost:8000/admin** tenemos nuestra interfaz de administrador configurada.

##Testeando la base de datos y sus modelos