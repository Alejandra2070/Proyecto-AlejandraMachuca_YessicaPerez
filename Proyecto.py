import json
def abrirArchivo():
    Campusjson=[]
    with open("Campus.json","r")as openfile:
     Campusjson=json.load(openfile)
    return Campusjson
def archivoGuardado(datos):
   with open("Campus.json","w")as outfile:
      json.dump(datos, outfile)

print("---------------------------")
print("----------MENÚ-------------")
print("---------------------------")
print("")
print("Bienvenidos, escoge una de las opciones de nuestro menú: \n1. Crear\n2. Leer\n3. Actualizar\n4. Eliminar ")
x = int(input("Elige la opción que deseas: "))
información=[]
if(x==1):
   info=abrirArchivo()
   for i in info[0]["alumnos"]:
      print("---------------------")
      print("id:", i["id"])
      print("nombre:", i["nombre"])
      print("apellido:", i["apellido"])
      print("dirección:", i["dirección"])
      print("acudiente:", i["acudiente"])
      print("número_celular:", i["número_celular"])
      print("número_fijo:", i["número_fijo"])
      print("estado:", i["estado"])
      print("riesgo:", i["riesgo"])
      print("------------------------")
      nuevocamper=input("puedes ingresar el nombre del nuevo camper:")
      apellidonuevo=input("puedes ingresar el nuevo apellido del camper:")
      direccionnueva=int(input("puedes ingresar la nueva direccion del camper: "))
      acudientenuevo=input("piedes ingresar el nombre del nuevo acudiente del camper:")
      numerocelularnuevo=int(input("puedes ingresar el nuevo numero de celular del camper:"))
      numerofijonuevo=int(input("puedes ingresar el nuevo numero fijo del camper:"))
      nuevoestado=input("puedes ingresar el nuevo estado del camper:")
      nuevoriesgo=input("puedes ingresar el nuevo riesgo:")
      campernuevo= {
         "nombre": nuevocamper,
         "apellido": apellidonuevo,
         "direccion": direccionnueva,
         "acudiente": acudientenuevo,
         "numero_celular": numerocelularnuevo,
         "numero_fijo": numerofijonuevo,
         "estado": nuevoestado,
         "riesgo": nuevoriesgo 
      }
      informacion=abrirArchivo()
      informacion[0]["alumnos"].append(campernuevo)
      archivoGuardado(informacion)
      print("se ha agregado el nuevo estudiante correctamente")  
print("")
