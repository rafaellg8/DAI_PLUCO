import pymongo
from datetime import date,datetime
class Database():
            try:
                  conn=pymongo.MongoClient()
                  print "Connected sucessfully!!!"
            except pymongo.errors.ConnectionFailure, e:
                  print "Could not connect to MongoDB: %s" %e    

            #definimos la base de datos a usar y coleccion
            db = conn.pluco
            collection = db.usuarios

            def getCollection(self):
                  try:
                        collection = db.usuarios
                  except:
                        return error
                  return collection

            def insertData(self,form):
                 #como da problemos con date time, convertimos primero la fecha
                 date = datetime.combine(form.birthday.data,datetime.min.time())
                 doc = {"username": form.username.data,"firstName": form.firstName.data,"secondName": form.secondName.data,"email": form.email.data,"creditCard": form.creditCard.data,"birthday": date,"address": form.address.data,"password": form.password.data,"confirm": form.confirm.data,"payMethod": form.paymethod.data}
                 #insertamos los datos en el documento
                 
                 self.collection.insert(doc)
                 print "Datos insertados"


            """> show databases
            local 0.078125GB
            > use pluco
            switched to db pluco
            > db.createCollection("usuarios")
            { "ok" : 1 }
            > show databases
            local 0.078125GB
            pluco 0.203125GB
            > show collections
            system.indexes
            usuarios
            > db


            puco.usuarios.insert({
                  author: ""
                  ......
                  })

            doc = {"name":"Alberto","surname":"Negron","twitter":"@Altons"}"""