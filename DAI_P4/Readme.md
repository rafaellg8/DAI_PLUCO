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

cramos los archivos [models.py](/plucoApp/models.py) y [testingPluco.py](/testingPluco.py)

##Configurando los modelos a un formulario

Creamos los foros en forms.py:
```
from django import forms
from .models import Comment,User,Forum

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userName','name','firstName','secondName','email','password','birthday',)

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('theme','title','commentText','url',)

class Forum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title','theme','asignature',)
```

Añadimos las urls en urls.py de pluco:
```
url(r'^foros/',include('foros.urls'))
```

En las urls de foros:
```
from django.conf.urls import patterns
from django.conf.urls import url

from foros import views

urlpatterns = patterns('',
    url(r'comentario', views.comment, name='comment'),
    url(r'^$', views.forums, name='forums'),
)
```

Y finalmente las vistas:

```
def comment(request):
    return render(request,'comentarios.html')

def forums(request):
    form = Forum
    return render(request,'foros.html', {'form': form})
```

[enlace models forms](http://tutorial.djangogirls.org/es/django_forms/index.html)

##Mostrar comentarios y añadir
```
def comment(request):
    if request.method =="POST":
        com = Comment.objects.order_by('idComment')[:1]
        for c in com:
            idC = c.idComment+1

        com = Comments(request.POST)

        userName = "usuariodeprueba"
        #validamos el formulario
        if com.is_valid():
            newComment = Comment(request.POST["theme"],idC,request.POST["title"],request.POST["commentText"],userName,request.POST["url"],datetime.date.today)
            return render(request,'comentarios.html')
    else:
        com = Comment()
    return render(request,'comentarios.html',{'commentForm':com},context_instance=RequestContext(request))
```    


##Mostrar comentarios ordenados por foros y temas
Para ello seguimos el punto 7 del tutorial de [Django](http://www.tangowithdjango.com/book17/chapters/models_templates.html).

Creamos una nueva vista en views.py de la app foros:
Esto seleccionará los foros ordeandos por temas
```
def theme(request,theme):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        #obtiene el foro asociado por tema
        form = Forum.objects.get(theme=theme)
        context_dict['forum_name'] = form.title

        # filtramos comentarios con tema del foro
        comm = Comment.objects.filter(theme=form)

        # Adds our results list to the template context under name pages.
        context_dict['comm'] = comm
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['theme'] = form
    except Forum.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'forosCat.html', context_dict)
```

Modificamos el showComments del views.py, para que muestre los comentarios ordeandos por tema y fecha también:
```
def showComments(request,theme):
    #obtenemos el foro asociado a un tema
    form = Forum.objects.get(theme=theme)
    #filtramos comentarios de un foro con un tema
    com = Comment.objects.filter(theme=form).order_by('date')
    context = {'com': com}
    #render
    return render(request,'comentarios.html',context)
```

Modificamos el urls.py principal de pluco:
```
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^plucoApp/', include('plucoApp.urls')),
    url(r'^foros/',include('foros.urls')),
    url(r'^comentario/',include('foros.urls')),
    url(r'^foros/theme/(?P<theme>[\w\-]+)/$', views.theme, name='theme'),
     # ADD THIS NEW TUPLE!
)
```

Finalmente modifico también los urls de la aplicación "foros":

```
urlpatterns = patterns('',
    url(r'(?P<theme>[\w\-]+)/$', views.showComments, name='theme'),
    url(r'nuevoComentario', views.comment, name='comment'),
    url(r'^$', views.showForums, name='forums'),
    url(r'foros', views.showForums, name='comment'),
)
```
Así reconoce la llama a showComments por un determinado tema de un comentario, la primera línea de las urls.

Ya sólo nos falta modificar los templates de los foros y comentarios para que muestren una lista de foros, y enlaces a esos comentarios de los foros.
1. foros.html:
```
<div>
  <h3>Foros</h3>
  <br><br><br>
  <h2>Lista de Foros</h2>

  {% if forum %}
             <ul>
                 {% for f in forum %}
                 <!-- Following line changed to add an HTML hyperlink -->
                 <li style="float: left;margin-right: 250px;margin-top: 50px"><a href="/foros/theme/{{ f.theme }}">{{ f.title }}</a></li>
                 {% endfor %}
             </ul>
  {% endif %}

</div>
```
Obtiene el parámetro forum de las vistas y muestra una lista con los enlaces a los foros



2. comenarios.html:
```
{% if com %}
    {% for c in com %}
      <ul style="border: 1px solid black">
          <h2>{{ c }}</h2>
          <li>{{c.title}}</li>
          <li>{{c.theme}}</li>
          <li>{{c.userName}}</li>
          <li>{{c.commentText}}</li>
          <li>{{c.url}}</li>
          <li>{{c.date}}</li>
      </ul>
          {% endfor %}
{% endif %}
```

Muestra los comentarios asociados al tema
