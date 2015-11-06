#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from wtforms import BooleanField
from wtforms import DateField
from wtforms import Form
from wtforms import PasswordField
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import validators
from wtforms import IntegerField
from wtforms import RadioField
from wtforms.fields.html5 import EmailField
"""
Clase principal para los registros.
Crea registros con campos asociados a cada entrada.
:param: Form
"""
class RegistrationForm(Form):
      username = TextField('Nombre usuario',[validators.Length(min=5,max=30),validators.required()])
      name = TextField('Nombre ',[validators.Length(min=5,max=30),validators.required()])
      firstName = TextField('Primer apellido',[validators.Length(min=5,max=30)])
      secondName = TextField('Segundo apellido',[validators.Length(min=5,max=30)])
      email = EmailField('Direccion email',[validators.Length(min=6,max=50),validators.Email()])
      # match = re.search(r'\w+@\w+', str)
      creditCard = TextField('Numero tarjeta Visa y 4 dígitos de control')
      validators.Regexp(r'\d{4}-\d{4}-\d{4}-\d{4}',message="Introduzca la #tarjeta separado por guiones ")
      birthday = DateField('Fecha nacimiento: dd/mm/aa',[validators.required()],format='%m/%d/%Y')

      address = TextAreaField('Direccion')

      password = PasswordField('Contrasenia',[validators.Length(min=7),validators.required(),validators.EqualTo('confirm',message='Contrasenias deben coincidir')])
      confirm = PasswordField('Repite contrasenia')


      paymethod = RadioField('Metodo Pago', choices=[('creditCard','Tarjeta Credito'),('efectivo','Pago Efectivo')])

      accept_tos = BooleanField('acepto los términos',[validators.required()])
