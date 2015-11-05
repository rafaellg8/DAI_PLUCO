import mandelbrot
from flask import Flask, session, redirect, url_for, escape, request
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		x1=int (request.form['x1'])
		y1=int (request.form['y1'])
		x2=float (request.form['x2'])
		y2=float (request.form['y2'])
		ancho=int (request.form['ancho'])
		ite=int (request.form['ite'])
		renderizaMandelbrot(x1, y1, x2, y2, ancho, ite, 'static/test1.png')
		return "<img src='/static/test1.png' alt='Dynamic Image' >"

	else:
		return "<form action='/' method='post'>\
<p>X1:<input type='text' name='x1'/></p>\
<p>Y1:<input type='text' name='y1'/></p>\
<p>X2:<input type='text' name='x2'/></p>\
<p>Y2:<input type='text' name='y2'/></p>\
<p>Ancho:<input type='text' name='ancho'/></p>\
<p>Iteraciones:<input type='text' name='ite'/></p>\
<p><input type='submit' value='PINTA'/></p>\
</form>"


def mostrar_form():
	return "<form action='/' method='post'>\
<p>X1:<input type='number' name='x1'/></p>\
<p>Y1:<input type='number' name='y1'/></p>\
<p>X2:<input type='number' name='x2'/></p>\
<p>Y2:<input type='number' name='y2'/></p>\
<p>Ancho:<input type='number' name='ancho'/></p>\
<p>Iteraciones:<input type='number' name='ite'/></p>\
<p><input type='submit' value='PINTA'/></p>\
</form>"


def hacer_img():
	x1=request.form['x1'],
	#y1=request.form['y1'],
	#x2=request.form['x2'],
	#y2=request.form['x2'],
	#ancho=request.form['ancho'],
	#ite=request.form['ite'],
	return "variable x1: %s" % x1
	#renderizaMandelbrot(x1, y1, x2, y2, ancho, ite, 'test.png')
	#return "<img src='/test.png' alt='Dynamic Image' >"

if __name__ == "__main__":
	app.run(debug=True)
