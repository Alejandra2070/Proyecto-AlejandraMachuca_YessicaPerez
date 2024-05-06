import json
#Función para abrir el json y cargar su contenido en una lista
def abrirarchivo():
    mijson=[]
    with open("campus.json",encoding="utf-8") as openfile:
        mijson=json.load(openfile)
    return mijson
#función para guardar datos en un archivo json
def guardarArchivo(miData):
    with open("campus.json","w") as outfile:
        json.dump(miData,outfile)
#Clase para representar a los campers
class campers:
    #constructor de la clase
    def __init__(self, id, usuario, contraseña, nombre, apellido, direccion, acudiente, numero_celular, numero_fijo, estado, riesgo):
        self.id=id
        self.usuario=usuario
        self.contraseña=contraseña
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.acudiente=acudiente
        self.numero_celular=numero_celular
        self.numero_fijo=numero_fijo
        self.estado=estado
        self.riesgo=riesgo
        print(campers)
#Clase que representa a los trainers
class trainers:
    #constructor de la clase tariners
    def __init__(self, id, nombre, rutaEntrenamiento, horario):
        self.id=id
        self.nombre=nombre
        self.rutaEntrenamiento=rutaEntrenamiento
        self.horario=horario
#Clase que representa una ruta de entrenamiento
class ruta:
    #constructor de la clase de ruta
    def __init__(self, nombre, modulo):
        self.nombre=nombre
        self.modulo=modulo
        self.camper=[]
    #método para agregar un camper a una ruta
    def agregarCamper(self, camper):
        if len(self.camper)<33:
            self.camper.append(camper)
            return True
        else:
            return False
#clase que representa al coordinador
class coordinador:
    #constructor de la clase coordinador
    def __init__(self, id, nombre, apellido, cargo):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo
    #método para subir la nota de los campers y cambiar su estado a aprobado si su promedio es mayor o igual a 60
    def subirNota(self, campers, notaTeorica, notaPractica):
        promedio=(notaTeorica*0.3+notaPractica*0.6)
        if promedio>=60:
            campers.estado="aprobado"
    #método para imprimir el estado de los campers
    def estadoCampers(self, campers):
        print("Estado de los campers: ")
        for camper in campers:
            print(f"Nombre: {camper.nombre}{camper.apellido}-Estado: {camper.estado}")
    #método para imprimir un reporte de los campers inscritos
    def reporteCampersInscritos(self):
        campersInscritos=[camper for camper in self.campers if camper.estado=="Inscrito"]
        print("Campers inscritos: ")
        for camper in campersInscritos:
            print(f"Nombre: {camper.nombre}{camper.apellido}")
    #método para imprimir un reporte de los campers aprobados
    def reporteCampersAprobados(self):
        campersAprobados=[camper for camper in self.campers if camper.estado=="Aprobado"]
        print("Campers aprobados: ")
        for camper in campersAprobados:
            print(f"Nombre: {camper.nombre}{camper.apellido}")
    #método para imprimir un reporte de los trainers trabajando en las rutas de entrenamiento
    def reporteTrainerTrabajando(self):
        print("Trainers trabajando: ")
        for ruta in self.rutaEntrenamiento:
            if hasattr(ruta, "trainer") and ruta.trainer:
                print(f"Ruta: {ruta.nombre},Trainer: {ruta.trainer.nombre}")
    #método para eliminar un camper de la lista de campers
    def eliminarCamper(self, listaCampers):
        idCamper=input("Ingrese el id del camper que desea eliminar: ")
        for camper in listaCampers:
            if camper.id==idCamper:
                listaCampers.remove(camper)
                print("Camper eliminado exitosamente")
                return 
        print("No se encontro ningún camper con ese id")
#clase que representa los reportes
class reporte:
    #constructor de la clase de reportes. Inicializa las listas de camper, trainers y rutas de entrenamiento, y crea una instancia de coordinador
    def __init__(self):
        self.campers=[]
        self.trainers=[]
        self.rutaEntrenamiento=[]
        self.coordinador=coordinador("6","Steven","Carvajal","Coordinador")
    #método para agregar un nuevo camper a la lista
    def camperNuevo(self, camper):
        self.campers.append(camper)
    #método para crear y agregar una nueva ruta de entrenamiento a la lista de rutas
    def nuevaRuta(self, id, nombre, modulo, capacidad_maxima):
        nuevaRuta=ruta(id, nombre, modulo, capacidad_maxima)
        self.rutaEntrenamiento.append(nuevaRuta)
    #método para asignar un camper a una ruta de entrenamiento
    def camperRuta(self, camper, rutaNombre):
        for ruta in self.rutaEntrenamiento:
            if ruta.nombre==rutaNombre:
                if ruta.agregarCamper(camper):
                    return True
                else:
                    return False
        return False
    #método para registrar un nuevo trainer en la lista de trainers
    def trainerRegistrar(self, trainer):
        self.trainers.append(trainer)
    #método para asignar un trainer a una ruta de entrenamiento
    def rutaTrainer(self, trainer, rutaNombre):
        for ruta in self.rutaEntrenamiento:
            if ruta.nombre==rutaNombre:
                ruta.trainer=trainer
                return True
        return False
    def reporteCampersInscritos(self):
        campersInscritos=[camper for camper in self.campers if camper.estado=="Inscrito"]
        print("Campers inscritos: ")
        for camper in campersInscritos:
            print(f"Nombre: {camper.nombre}{camper.apellido}")
    def reporteCampersAprobados(self):
        campersAprobados=[camper for camper in self.campers if camper.estado=="Aprobado"]
        print("Campers aprobados: ")
        for camper in campersAprobados:
            print(f"Nombre: {camper.nombre}{camper.apellido}")
    def reporteTrainerTrabajando(self):
        print("Trainers trabajando: ")
        for ruta in self.rutaEntrenamiento:
            if hasattr(ruta, "trainers") and ruta.trainer:
                print(f"Ruta: {ruta.nombre},Trainer: {ruta.trainer.nombre}")
#imprime el menú principal   
    print("\n---------MENÚ----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Coordinador")
    print("4. Salir")
#solicita al usuario que elija una opción
opc=input("Elige una de nuestras opciones: ")
#si el usuario elige la opción 1 
if opc=="1":
    #imprime el menú de campers
    print("\n-----Menú campers--------")
    print("1. Revisar mi información")
    print("2. Salir del programa")
    #solicita al usuario que elija una opción del menú de campers
    x=int(input("Elige una de nuestras opciones: "))
    #si el usuario elije la opción 1
    if x==1:
        #abre el archivo json y muestra la información de cada camper
        miInfo=abrirarchivo()
        for i in miInfo[0]["campers"]:
            print("------------------------")
            print("ID:",i["id"])
            print("Usuario:",i["usuario"])
            print("Contraseña:",i["contrasena"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Dirección:",i["direccion"])
            print("Acudiente:",i["acudiente"])
            print("Número de celular:",i["numero_celular"])
            print("Número fijo:",i["numero_fijo"])
            print("Estado:",i["riesgo"])
            print("Riesgo:",i["riesgo"])
            print("-------------------------")
            print("")
    elif x==2:
        print("Hasta luego Camper. Vuelve pronto!")
        #si elije la opción 2
elif opc=="2":
        #imprime el menú de trainers
        miInfo=abrirarchivo()
        print("-------Menú trainers----------")
        print("1. Estado de los campers")
        print("2. Ruta de los trainers")
        print("3. Reportes")
        print("4. Salir del programa")
        #solicita al usuario que elija una opción del menú de trainers
        x=int(input("Elige una de nuestras opciones: "))
        #si el usuario elige la opción 1
        if x==1:
            print("Elige el grupo de los campers:")
            print("1. Grupo t1")
            print("2. Grupo t2")
            print("3. Grupo t3")
            #solicita al usuario que elija un grupo de campers
            grupo=int(input("Elige una de las opciones: "))
            #abre el archivo json y muestra el estado de los campers del grupo seleccionado
            miInfo=abrirarchivo()
            if grupo == 1:
                print("Este es el estado de los campers del grupo t1")
                for camper in miInfo[0]["campers"]:
                    if camper["grupo"]=="t1":
                        print(f"Nombre: {camper["nombre"]}{camper["apellido"]}, ID: {camper["id"]}, Estado: {camper["estado"]}")
            elif grupo == 2:
                print("Este es el estado de los campers del grupo t2")
                for camper in miInfo[0]["campers"]:
                    if camper["grupo"]=="t2":
                        print(f"Nombre: {camper["nombre"]}{camper["apellido"]}, ID: {camper["id"]}, Estado: {camper["estado"]}")
            elif grupo == 3:
                print("Este es el estado de los campers del grupo t3")
                for camper in miInfo[0]["campers"]:
                    if camper["grupo"]=="t3":
                        print(f"Nombre: {camper["nombre"]}{camper["apellido"]}, ID: {camper["id"]}, Estado: {camper["estado"]}")
        #si el usuario elige la opción 2
        elif x==2:
            #abre el archivo json y muestra la ruta de los trainers
            miInfo=abrirarchivo()
            print("Esta es la ruta de los trainers: ")
            for ruta in miInfo[0]["ruta"]:
                print(f"Nombre del trainer: {ruta["trainer"]}, Nombre de la ruta: {ruta["nombre"]}, Módulo: {ruta["modulo"]}, Capacidad: {ruta["capacidad_maxima"]}")
        #si el usuario elige la opción 3
        elif x==3:
            #abre el archivo json y crea una instancia de reporte
            miInfo=abrirarchivo()
            reporte_instancia=reporte()
            #itera sobre los campers en el archivo json y los agrega a la instancia de reporte
            for camper in miInfo[0]["campers"]:
                nuevo_camper=campers(camper["id"], camper["usuario"], camper["contrasena"], camper["nombre"], camper["apellido"], camper["direccion"], camper["acudiente"], camper["numero_celular"], camper["numero_fijo"], camper["estado"], camper["riesgo"])
                reporte_instancia.camperNuevo(nuevo_camper)
            #genera y muestra los reportes de campers inscritos, campers aprobados y trainers trabajando
            reporte_instancia.reporteCampersInscritos()
            reporte_instancia.reporteCampersAprobados()
        #si el usuaro elige la opción 4, sale del programa
        elif x==4:
            print("Hasta luego Trainer. Vuelve pronto!")
elif opc=="3":
        print("--------Menú coordinador----------")
        print("1. Registrar campers")
        print("2. Actualizar datos nuevos del camper")
        print("3. Reporte campers inscritos")
        print("4. Reporte de campers aprobados")
        print("5. Estado de los campers")
        print("6. Campers con bajo rendimiento")
        print("7. Agregar rutas de entrenamiento")
        print("8. Asignar campers a la ruta de entrenamiento")
        print("9. Agregar nuevos trainers")
        print("10. Reporte de trainers trabajando")
        print("11. Eliminar campers")
        print("12. Eliminar trainers")
        print("13. Eliminar rutas")
        print("14. Salir del programa")
        x=int(input("Elige una de nuestras opciones: "))
        if x==1:
            #solicitar detalles del nuevo camper al usuario
            id=int(input("Ingrese el id del nuevo camper: "))
            usuario=int(input("Ingrese el usuario del nuevo camper: "))
            contraseña=input("Ingrese la contraseña del nuevo camper: ")
            nombre=input("Ingrese el nombre del nuevo camper: ")
            apellido=input("Ingrese el apellido del nuevo camper: ")
            direccion=input("Ingrese la dirección del nuevo camper: ")
            acudiente=input("Ingrese el nombre y apellido del acudiente del nuevo camper: ")
            numero_celular=int(input("Ingrese el número de celular del nuevo camper: "))
            numero_fijo=input("Ingrese el número fijo del nuevo camper: ")
            estado=input("Ingrese el estado del nuevo camper: ")
            riesgo=input("Ingrese el riesgo del nuevo camper: ")
            #crear un diccionario con la información del nuevo camper
            nuevo_camper= {
                "id": id,
                "usuario": usuario,
                "contrasena": contraseña,
                "nombre": nombre,
                "apellido": apellido,
                "direccion": direccion,
                "acudiente": acudiente,
                "numero_celular": numero_celular,
                "numero_fijo": numero_fijo,
                "estado": estado,
                "riesgo": riesgo,
                
            }
            #abrir el archivo json y agregar el nuevo camper
            miInfo = abrirarchivo()
            miInfo[0]["campers"].append(nuevo_camper)
            guardarArchivo(miInfo)
            #informa al usuario que el nuevo camper se ha registrado exitosamente
            print("El nuevo camper se ha registrado exitosamente")
        elif x==2:
            #abrir el archivo json y obtener el id del camper que se desea actualizar
            miInfo=abrirarchivo()
            idCamper=int(input("Ingrese el id del camper al que desea actualizar datos: "))
            camperEncontrado=None
            #buscar el camper en la lista de campers
            for camper in miInfo[0]["campers"]:
                if camper ["id"]==idCamper:
                    camperEncontrado=camper
                    break
            if camperEncontrado:
                #si se encuentra al camper, imprimir las opciones de datos que se pueden actualizar
                print("Seleccione cuáles datos del camper desea utilizar: ")
                print("1. Usuario")
                print("2. Contraseña")
                print("3. Nombre")
                print("4. Apellido")
                print("5. Dirección")
                print("6. Acudiente")
                print("7. Número de celular")
                print("8. Número fijo")
                print("9. Estado")
                print("10. Riesgo")
                print("11. Grupo")
                #solicitar al usuario la opción que desea actualizar
                opc=int(input("Ingrese la opción que desea actualizar: "))
                if opc==1:
                    #actualizar el usuario del camper
                    nuevoUsuario= input("Ingrese el nuevo usuario del camper: ")
                    camperEncontrado["usuario"]=nuevoUsuario
                elif opc ==2:
                    #actualizar la contraseña del camper
                    nuevaContraseña=("Ingrese la nueva contraseña del camper: ")
                    camperEncontrado["contraseña"]=nuevaContraseña
                elif opc==3:
                    #actualizar el nombre del camper
                    nuevoNombre=input("Ingrese el nuevo nombre el camper: ")
                    camperEncontrado["nombre"]= nuevoNombre
                elif opc ==4:
                    #actualizar el apellido del camper
                    nuevoApellido=input("Ingrese el nuevo apellido del camper: ")
                    camperEncontrado["apellido"]=nuevoApellido
                elif opc==5:
                    #actualizar la dirección del camper
                    nuevaDireccion=input("Ingrese la nueva dirección del camper: ")
                    camperEncontrado["direccion"]=nuevaDireccion
                elif opc ==6:
                    #actualizar el acudiente del camper
                    nuevoAcudiente=input("Ingrese el nuevo nombre y apellido del acudiente del camper: ")
                    camperEncontrado["acudiente"]=nuevoAcudiente
                elif opc==7:
                    #actualizar el número celular del camper
                    nuevoNumeroCelular=input("Ingrese el nuevo número de celular del camper: ")
                    camperEncontrado["numero_celular"]=nuevoNumeroCelular
                elif opc ==8:
                    #actualizar el número fijo del camper
                    nuevoNumeroFijo=input("Ingrese el nuevo número fijo del camper: ")
                    camperEncontrado["numero_fijo"]=nuevoNumeroFijo
                elif opc==9:
                    #actualizar el estado del camper
                    nuevoestado=input("Ingrese el nuevo estado del camper: ")
                    camperEncontrado["estado"]=nuevoestado
                elif opc==10:
                    #actualizar el riesgo del camper
                    nuevoRiesgo=input("Ingrese el nuevo riesgo del camper: ")
                    camperEncontrado["riesgo"]=nuevoRiesgo
                elif opc ==11:
                    #actualizar el grupo del camper
                    nuevogrupo=input("Ingrese el nuevo grupo del camper: ")
                    camperEncontrado["grupo"]=nuevogrupo
                else:
                    print("Esta opción no existe. Por favor elige otra.")
                guardarArchivo(miInfo)
                print("los datos del camper se han actualizado exitosamente")
            else:
                print("no se encontro ningun camper con ese id")
        #esta parte del código verifica que eligió la opción para generar el reporte de campers inscritos          
        elif x==3: 
            #abre el archivo json para obtener la información necesaria
            miInfo=abrirarchivo()
            print("Reporte de campers inscritos: ")
            #iinicializa una variable booleano para verificar si hay campers inscritos
            campersIncritos = False
            for camper in miInfo[0]["campers"]:
                if camper["estado"] == "inscrito":
                    print(f"Nombre: {camper["nombre"]} {camper["apellido"]}")
                    print(f"ID: {camper["id"]}")
                    print(f"Estado: {camper["estado"]}")
                    print("------------------------")
                    campersIncritos = True
            if not campersIncritos:
                print("No hay campers inscritos actualmente.")
        #verifica la opción 4 para generar el reporte de campers aprobados
        elif x==4:
            #abre el archivo json para obtener la información necesaria
            miInfo=abrirarchivo()
            #inicializa una lista para almacenar campers aprobados
            campers_aprobados=[]
            for camper in miInfo[0]["campers"]:
                if camper["Estado: "]=="aprobado":
                    campers_aprobados.append(camper)
            if campers_aprobados:
                print("Reporte de campers aprobados: ")
                for camper in campers_aprobados:
                    print(f"ID: {camper["id"]}, Nombre:{camper["nombre"]}{camper["apellido"]}, Estado:{camper["estado"]}")
            else:
                print("No hay campers aprobados en este momento")
        #verifica que eligió la opción 5 y muestra el estado de los campers
        elif x==5:
            #abre el archivo json para obtener la información necesaria
            miInfo=abrirarchivo()
            print("Estado de los campers: ")
            for camper in miInfo[0]["campers"]:
                print(f"ID: {camper["id"]}, Nombre: {camper["nombre"]}{camper["apellido"]}, Estado: {camper["estado"]}")
        #verifica la opción 6 y muestra los campers con bajo rendimiento
        elif x==6:
            #abre el archivo json para obtener la información necesaria
            miInfo=abrirarchivo()
            print("Campers con bajo rendimiento: ")
            for camper in miInfo[0]["campers"]:
                if camper["estado"]=="bajo rendimiento":
                    print(f"ID: {camper["id"]}, Nombre: {camper["nombre"]}{camper["apellido"]}")
        #verifica la opción 7 y permite agregar nuevas rutas de entrenamiento
        elif x==7:
            #solicita al usuario que ingrese los detalles de la nueva ruta
            id=int(input("Ingrese el id de la nueva ruta: "))
            nombre=input("Ingrese el nombre de la nueva ruta: ")
            modulo=input("Ingrese los módulos de la nueva ruta separados por comas: ").split(",")
            capacidad_maxima=int(input("Ingrese la capacidad máxima de campers en la ruta: "))
            #crea un diccionario con los detalles ingresados
            nueva_ruta={
                "id": id,
                "nombre": nombre,
                "modulo": modulo,
                "capacidad_maxima": capacidad_maxima,
            }
            #abre el archivo json para obtener la información necesaria
            miInfo = abrirarchivo()
            miInfo[0]["ruta"].append(nueva_ruta)
            #agrega la nueva ruta al archivo json
            guardarArchivo(miInfo)
            print("La nueva ruta fue creada exitosamente")
        #verifica la opción 8 y permite asignar un camper a una ruta de entrenamiento
        elif x==8:
            miInfo=abrirarchivo()
            #solicita al usuario que ingrese el id del camper y el nombre de la ruta de entrenamiento
            idCamper=int(input("Ingrese el id del camper: "))
            nombreRuta=input("Ingrese el nombre de la ruta de entrenamiento: ")
            camperEncontrado= None
            #busca el camper y la ruta de entrenamiento correspondientes en el archivo json
            for camper in miInfo[0]["campers"]:
                #si se encuentra el camper y la ruta de entrenamiento
                if camper["id"]==idCamper:
                    camperEncontrado=camper
                    break
            if camperEncontrado:
                rutaEncontrada= None
                for ruta in miInfo[0]["ruta"]:
                    if ruta["nombre"]==nombreRuta:
                        rutaEncontrada=ruta
                        break
                if rutaEncontrada:
                    #intenta asignar el camper a la ruta de entrenamiento
                    if reporte.camperRuta(camperEncontrado, nombreRuta):
                        print("El camper ha sido asignado a la ruta de entrenamiento")
                    else:
                     print("La ruta de entrenamiento seleccionada no tiene cupos disponibles")
                else:
                 print("La ruta de entrenamiento especificada no existe")
            else:
                print("El camper con el ID ingresado no fue encontrado")
        #verifica la opción 9 y permite registrar un nuevo trainer
        elif x==9:
            #solicita al usuario que ingrese el id, nombre, ruta y horario del nuevo trainer
            id=int(input("Ingrese el id del nuevo trainer: "))
            nombre=input("Ingrese el nombre del nuevo trainer: ")
            ruta=input("Ingrese la ruta del nuevo trainer: ")
            horario=input("Ingrese el horario del nuevo trainer: ")
            #crea un diccionario con los detalles ingresados 
            nuevo_trainer={
                "id":id,
                "nombre":nombre,
                "ruta":ruta,
                "horario":horario,
            }
            #abre el archivo json para obtener la información necesaria
            miInfo=abrirarchivo()
            miInfo[0]["trainers"].append(nuevo_trainer)
            #agrega el nuevo trainer al archivo json
            guardarArchivo(miInfo)
            print("El nuevo trainer fue registrado exitosamente")
        #verifica la opción 10 y genera reporte de los trainers trabajando
        elif x==10:
            #abre el archivo json para obtener la información necesaria sobre los trainers
            miInfo=abrirarchivo()
            trainersTrabajando = False
            print("Reporte de trainers trabajando: ")
            for trainer in miInfo[0]["trainers"]:
                #si un trainer tiene una ruta de entrenamiento asignada, imprime su nombre, ruta de entrenamiento y horario
                if trainer["rutaEntrenamiento"]:
                    print(f"Nombre del trainer: {trainer["nombre"]}")
                    print(f"Ruta de entrenamiento: {trainer["rutaEntrenamiento"]}")
                    print(f"Horario: {trainer["horario"]}")
                    trainersTrabajando=True
            if not trainersTrabajando:
                print("No hay trainers trabajando actualmente")
        #verifica la opción 11 y permite eliminar un camper
        elif x==11:
            miInfo=abrirarchivo()
            #solicita al usuario que ingrese el id del camper que desea eliminar
            eliminarCamper = input("Ingrese el id del camper que quiere eliminar: ")
            camperEncontrado = False
            for grupo in miInfo:
                for camper in grupo["campers"]:
                    #busca el camper en el archivo json y lo elimina si se encuentra
                    if camper["id"]==eliminarCamper:
                        grupo["campers"].remove(camper)
                        camperEncontrado=True
                        break
                if camperEncontrado:
                    break
            if camperEncontrado:
                #si se elimina el camper con exito, guarda los cambios en el archivo json
                guardarArchivo(miInfo)
                print("El camper ha sido eliminado exitosamente")
            else:
                print("El camper no ha sido encontrado")
        #verifica la opción 12 y permite eliminar un trainer    
        elif x==12:
            miInfo = abrirarchivo()
            #solicita al usuario que ingrese el id del trainer que desea eliminar
            eliminarTrainer = input("Ingrese el ID del trainer que quiere eliminar: ")
            trainerEncontrado = False
            for grupos in miInfo:
                for trainer in grupos["trainers"]:
                    #busca el trainer en el archivo json y lo elimina si se encuentra
                    if trainer["id"] == eliminarTrainer:
                        grupos["trainers"].remove(trainer)
                        trainerEncontrado = True
                        break
                if trainerEncontrado:
                    break
            if trainerEncontrado:
                #si se elimina el trainer con exito, guarda los cambios en el archivo json
                guardarArchivo(miInfo)
                print("El trainer ha sido eliminado correctamente")
            else:
                print("El trainer no ha sido encontrado")
        #verifica la opción 13 y permite eliminar una ruta
        elif x==13:
            miInfo = abrirarchivo()
            #solicita al usuario que ingrese el nombre de la ruta que desea eliminar
            eliminarRuta=input("Ingrese el nombre de la ruta que desea eliminar: ")
            rutaEncontrada= False
            for grupo in miInfo:
                for ruta in grupo["ruta"]:
                    #busca la ruta en el archivo json y la elimina si se encuentra
                    if ruta["nombre"]==eliminarRuta:
                        grupo["ruta"].remove(ruta)
                        rutaEncontrada=True
                        break
                if rutaEncontrada:
                    break
            if rutaEncontrada:
                #si se elimina la ruta con exito, guarda los cambios en el archivo json
                guardarArchivo(miInfo)
                print("La ruta ha sido eliminada correctamente")
            else: 
                print("La ruta no ha sido encontrada")
elif opc=="4":
    print("Gracias por usar nuestro programa. Vuelve pronto.")