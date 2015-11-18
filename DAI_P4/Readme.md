##Practica 4 Tango , Rango with Django

##Algunos comandos
###Crear proyecto
```
django-admin.py startproject pluco
```
###Run y migrate

python pluco/manage.py migrate

python pluco/manage.py runserver

###Crear una app
**Dentro del directorio**
python manage.py startapp plucoApp

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