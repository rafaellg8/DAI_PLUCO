#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rafael Lachica Garrido

PLUCO - RLG

Plataforma Universitaria Comparticion Conocimiento

Granada 2015-2016

"""

import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask import request
from flask import Flask
from wtforms import form, Form
import random
import shelve
from registration import RegistrationForm
import anydbm
app = Flask(__name__)

"""
Ruta principal, acceso al index
:param /: ruta principal

Llama a render template y crea el archivo index a traves del template.
"""
@app.route('/')
def index():
    url_for('static',filename='style.css')
    url_for('static',filename='hijo.html')
    if 'username' in session:
        session['recentpage']='index';
        return render_template('hijo.html',usuario = (session['username']),recentpage = (session['recentpage']))
    else:
        return render_template('hijo.html',usuario = None)

    #devuelve la pagina hola.html, y le pasa como parametro el nombre de usuario
@app.route('/user/<user>')
def hello_world(user=None):
    #return render_template('hola.html', usuario=user)
    return 'Bienvenido %s' % user

"""
Controlador de login.
Manejando sesiones.
"""
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        #Comprobar si el usuario existe, si no existe, redireccionamos a la pagina de error de usuario
        form = RegistrationForm()
        if (form.checkuser(request.form['username'],request.form['password'])):
            return redirect(url_for('index'))
        else:
            return render_template('errorUser.html',usuario = None)

    #Mostrar el login si no se ha hecho aún el POST
    return render_template('login.html',usuario = None)



"""
Controlador logout
Manejo de sesiones
"""
@app.route('/logout')
def logout():
        #remove the username from the session
        session.pop('username',None)
        return redirect(url_for('index'))

#secret key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

"""
Controlador registro.
Si el registro es correcto, da la informacion del usuario.
Sino, ofrece la pagina de registros
"""
@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
            form.databases()
            return render_template('hijo.html',usuario=form.username.data)

    return render_template('register.html',form=form)

@app.route('/contact')
def contact():
    if 'username' in session:
        session['recentpage']='index';
        return render_template('autor.html',usuario = (session['username']),recentpage = (session['recentpage']))
    else:
        return render_template('autor.html',usuario = None,recentpage = None)

@app.route('/recentpage')
def recentpage():
    return redirect(url_for(session['recentpage'],usuario = (session['username']),recentpage = (session['recentpage'])))

"""
Gestion de errores, pagina no encontrada
:param 404: error pagina no encontrada
"""
@app.errorhandler(404)
def page_not_found(error):
    return """<h1>Pagina no encontrada</h1>
    <a href="/">volver</a>""", 404

"""
inicio de la app
"""
if __name__ == '__main__':
    app.debug = True #modo debug activado
    app.run(host='0.0.0.0',port=1111)
