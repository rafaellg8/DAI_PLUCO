from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask import request
from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def index():
    url_for('static',filename='style.css')
    url_for('static',filename='principal.html')
    return render_template('principal.html')

    #devuelve la pagina hola.html, y le pasa como parametro el nombre de usuario
@app.route('/user/<user>')
def hello_world(user=None):
    #return render_template('hola.html', usuario=user)
    return 'Bienvenido %s' % user

#Gestion de errores, pagina no encontrada
@app.errorhandler(404)
def page_not_found(error):
    return """<h1>Pagina no encontrada</h1>
    <a href="/">volver</a>""", 404


if __name__ == '__main__':
    app.debug = True #modo debug activado
    app.run(host='0.0.0.0',port=1111)
