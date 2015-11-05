import mandelbrot
from flask import Flask, session, redirect, url_for, escape, request
from flask import request
from flask import Flask
from xml.etree import ElementTree as ET
import svgwrite
import random
app = Flask(__name__)


@app.route('/')
def index():
    url_for('static',filename='style.css')
    url_for('static',filename='index.html')
    #return ("<img src='static/image.jpg' width=120 height=120 alt='myimage'>")
    #devuelve la pagina index de forma estatica
    return""" <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Index</title>
        <link rel="stylesheet" type="text/css" href="../static/style.css">
    </head>
    <body>
        <h1>HELLO WORLD!</h1>
        <img src="static/image.jpg" alt="image" style="float: left">
        <h1 style="float: left"><a href="imagen">crear imagen</a></h1>

    </body>
    </html>
    """
    #return render_template('index.html')
@app.route('/imagen',methods=['GET', 'POST'])
def crearImagen():
    if request.method == 'POST':
        width = (int(request.form['widht']))
        x1 = (int(request.form['x1']))
        y1 = (int(request.form['y1']))
        y2 = (int(request.form['y2']))
        x2 = (int(request.form['x2']))
        numIter = (int(request.form['numIter']))
        color = (request.form['color'])
        paleta = [[255,0,0],[255,0,0],[255,0,0]]
        mandelbrot.renderizaMandelbrotBonito(x1,y1,x2,y2,width,numIter,"static/imagen.png",paleta,3)
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Index</title>
            <link rel="stylesheet" type="text/css" href="../static/style.css">
        </head>
        <body>

        <img src='/static/imagen.png' alt='Dynamic Image' >
        </body>
        </html>"""
    else:
        return '''<form action="/imagen" method="post">
            <p>ancho<input type="text" name="widht"/></p>
            <p>x1<input type="text" name="x1" /></p>
            <p>x2<input type="text" name="x2" /></p>
            <p>y1<input type="text" name="y1" /></p>
            <p>y2<input type="text" name="y2" /></p>
            <p>numero de iteraciones<input type="text" name="numIter"/></p>
            <p>color<input type="color" name="color"/></p>
            <p><input type="submit" value="Crear imagen"/></p>
        </form>'''

@app.route('/svg')
def imagenSV():
    widht = (str(random.randint(1,1000)))
    height = (str(random.randint(1,1000)))
    radio = (str(random.randint(10,100)))
    rand = random.randint(1,4)
    color = random.choice(['red','green','blue','yellow','orange','pink','black'])
    color = (str(color))
    #Circulo 1,rectangulo 2, linea 3, triangulo 4
    if (rand==1):
            return """
                <!DOCTYPE html>
                <html>
                    <body>
                    <svg height="""+height+""" width="""+widht+""">
                        <circle cx="""+(str(random.randint(1,100)))+""" cy="""+(str(random.randint(1,100)))+""" r="""+radio+""" stroke="black" stroke-width="3" fill="""+color+""" />
                        Sorry, your browser does not support inline SVG.
                    </svg>
                    </body>
                </html>"""

    elif (rand==2):
        return """
        <!DOCTYPE html>
        <html>
            <body>
             <svg width="""+widht+""" height="""+height+""">
                <rect width="""+widht+""" height="""+height+""" fill="""+color+""" style="stroke-width:3;stroke:rgb(0,0,0)" />
            </svg>
            </body>
        </html>"""
    elif (rand==3):
        return """
        <!DOCTYPE html>
        <html>
            <body>
             <svg width="""+widht+""" height="""+height+""">
                <rect width="""+widht+""" height="""+height+""" fill ="""+color+""" style=;stroke-width:3;stroke:rgb(0,0,0)" />
            </svg>
            </body>
        </html>"""
    elif (rand==4):
        return """
        <!DOCTYPE html>
        <html>
            <body>
                <svg height="""+height+""" width="""+widht+""">
                    <polygon points="200,10 250,190 160,210" fill = """+color+""" style=stroke:purple;stroke-width:1" />
                </svg>
            </body>
        </html>
        """

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
