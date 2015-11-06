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
    return render_template('hijo.html',usuario = None)

    #devuelve la pagina hola.html, y le pasa como parametro el nombre de usuario
@app.route('/user/<user>')
def hello_world(user=None):
    #return render_template('hola.html', usuario=user)
    return 'Bienvenido %s' % user

"""
Controlador registro.
Si el registro es correcto, da la informacion del usuario.
Sino, ofrece la pagina de registros
"""
@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
            return render_template('hijo.html',usuario=form.username.data)

    return render_template('register.html',form=form)

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
