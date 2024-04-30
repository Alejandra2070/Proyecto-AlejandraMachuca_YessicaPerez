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
print("Bienvenidos, escoge una de las opciones de nuestro menú: \n1. Campers\n2. Trainers\n3. Coordinador")
x = int(input("Elige la opción que deseas: "))
información=[]
if(x==1):
   info=abrirArchivo()
   for i in info[0]["alumnos"]:
       print("ingrese la contraseña: ")
       print(input(""))
       idAlumno=input("Ingrese el ID del camper")
       idAlumno=int(input(""))

       def main():
          campers=input("Ingrese su nombre de usuario: ")
          contraseña=input("Ingrese su contraseña: ")
          verificarContraseña(campers, contraseña)
       print("----------------------")
       print("ID:", i["id"])
       print("Nombre:", i["nombre"])
       print("Apellido:", i["apellido"])
       print("Acudiente:", i["acudiente"])
       print("Direccion:", i["direccion"])
       print("Numero de celular:", i["numero_celular"])
       print("Numero fijo", i["numero_fijo"])
       print("Estado:", i["estado"])
       print("Riesgo:", i["riesgo"])
       print("----------------------")
       print("")
       def contraseñasCampers():
          with open("contraseñas.json","r")as file:
             return json.load(file)
       def verificarContraseña(campers, contraseña):
          contraseñas=contraseñasCampers()
          if campers in contraseñas["campers"]and contraseñas["campers"][campers]==contraseñas:
             print("Contraseña correcta")
          else:
             print("Contraseña incorrecta")
       def main():
          campers=input("Ingrese su nombre de usuario: ")
          contraseña=input("Ingrese su contraseña: ")
          verificarContraseña(campers, contraseña)
if(x==2):
   info=abrirArchivo
   for i in ["2"]:
    print("------------------------")
    print("Trainer:", i["trainer"])
    print("Salón", i["salon"])
    print("Ruta", i["ruta"])
    print("Módulo", i["modulo"])
    print("Hora", i["hora"])
if(x==3):
   info=abrirArchivo, {
      "coordinador"
   }
   print("tú puedes:)")


