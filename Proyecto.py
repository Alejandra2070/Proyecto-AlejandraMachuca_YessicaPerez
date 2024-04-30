import json
def abrirArchivo():
    Campus=[]
    with open("Campus.json","r")as openfile:
     Campus=json.load(openfile)
    return Campus
def archivoGuardado(datos):
   with open("Campus.json","w")as outfile:
      json.dump(datos, outfile)

print("---------------------------")
print("----------MENÚ-------------")
print("---------------------------")
print("")
print("Bienvenidos, escoge una de las opciones de nuestro menú: \n1. Campers\n2. trainers\n3. coordinador")
x = int(input("Elige la opción que deseas: "))
información=[]
if(x==1):
   info=abrirArchivo()
   for i in info[0]["alumnos"]:
       print("ingrese la contraseña del camper")
       print(input(""))
       print("----------------------")
       print("ID:", i["id"])
       print("Nombre:", i["nombre"])
       print("Apellido:", i["apellido"])
       print("Acudiente:", i["acudiente"])
       print("direccion:", i["direccion"])
       print("Numero de celular:", i["numero_celular"])
       print("Numero fijo", i["numero_fijo"])
       print("Estado:", i["estado"])
       print("Riesgo:", i["riesgo"])
       print("----------------------")
       print("")


