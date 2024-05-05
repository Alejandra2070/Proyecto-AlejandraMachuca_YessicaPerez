import json
def abrirarchivo():
    mijson=[]
    with open("campus.json","r") as openfile:
        mijson=json.load(openfile)
    return mijson
def guardarArchivo(miData):
    with open("campus.json","w") as outfile:
        json.dump(miData,outfile)

class campers:
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
class trainers:
    def __init__(self, id, nombre, rutaEntrenamiento, horario):
        self.id=id
        self.nombre=nombre
        self.rutaEntrenamiento=rutaEntrenamiento
        self.horario=horario
class ruta:
    def __init__(self, nombre, modulos):
        self.nombre=nombre
        self.modulos=modulos
        self.camper=[]
    def agregarCamper(self, camper):
        if len(self.camper)<33:
            self.camper.append(camper)
            return True
        else:
            return False
class coordinador:
    def __init__(self, id, nombre, apellido, cargo):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo
    def subirNota(self, campers, notaTeorica, notaPractica):
        promedio=(notaTeorica*0.3+notaPractica*0.6)
        if promedio>=60:
            campers.estado="aprobado"
class reporte:
    def __init__(self):
        self.campers=[]
        self.trainers=[]
        self.rutaEntrenamiento=[]
        self.coordinador=coordinador("6","Steven","Carvajal","Coordinador")
    def camperNuevo(self, camper):
        self.campers.append(camper)
    def nuevaRutaEntrenamiento(self, id, nombre, modulos, capacidad):
        rutaEntrenamiento=ruta(id, nombre, modulos, capacidad)
        self.ruta.append(rutaEntrenamiento)
    def camperRuta(self, camper, rutaNombre):
        for ruta in self.rutaEntrenamiento:
            if ruta.nombre==rutaNombre:
                if ruta.agregarCamper(camper):
                    return True
                else:
                    return False
    def trainerRegistrar(self, trainer):
        self.trainers.append(trainer)
    def rutaTrainer(self, trainer, rutaNombre):
        for ruta in self.rutaEntrenamiento:
            if ruta.nombre==rutaNombre:
                ruta.trainer=trainer
                return True
        return False
    def reporteCampersInscritos(self):
        campersInscritos=[camper for camper in self.campers if camper.estado=="inscrito"]
        print("Campers inscritos: ")
        for camper in campersInscritos:
            print(f"{camper.nombre}{camper.apellido}")
    def reporteCampersAprobados(self):
        campersAprobados=[camper for camper in self.campers if camper.estado=="aprobado"]
        print("Campers aprobados: ")
        for camper in campersAprobados:
            print(f"{camper.nombre}{camper.apellido}")
    def reporteTrainerTrabajando(self):
        print("Trainers trabajando: ")
        for ruta in self.rutaEntrenamiento:
            if hasattr(ruta, "trainer") and ruta.trainer:
                print(f"Ruta: {ruta.nombre},trainer: {ruta.trainer.nombre}")

    print("\n-----------------Menú-----------------")
    print("1. Registrar campers")
    print("2. Rutas de entrenamiento")
    print("3. Campers ruta de entrenamiento")
    print("4. Trainers")
    print("5. Ruta de entrenamiento a trainers")
    print("6. Reporte campers inscritos")
    print("7. Reporte de campers aprobados")
    print("8. Reporte de trainers trabajando")
    print("9. Salir")
opc=input("Elija una de las opciones de nuestro menú: ")
if opc=="1":
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
    miInfo = abrirarchivo()
    miInfo[0]["campers"].append(nuevo_camper)
    guardarArchivo(miInfo)
    print("El nuevo camper se ha registrado exitosamente")
elif opc =="2":
    id=int(input("Ingrese el id de la nueva ruta: "))
    nombre=input("Ingrese el nombre de la nueva ruta: ")
    modulos=input("Ingrese los módulos de la nueva ruta separados por comas: ").split(",")
    capacidad=int(input("Ingrese la capacidad máxima de campers en la ruta: "))
    nueva_ruta={
        "id": id,
        "nombre": nombre,
        "modulo": modulos,
        "capacidad_maxima": capacidad,
    }
    miInfo = abrirarchivo()
    miInfo[0]["ruta"].append(nueva_ruta)
    guardarArchivo(miInfo)
    print("la nueva ruta fue creada exitosamente")
elif opc=="3":
    idCamper=int(input("Ingrese el id del camper: "))
    rutaNombre=input("Ingrese el nombre de la ruta: ")
    camper=next((camper for camper in reporte.campers if camper.id==idCamper), None)
    if camper:
        if reporte.camperRuta(camper, rutaNombre):
            print("Camper asignado a la ruta: ")
        else:
            print("El camper no pudo ser asignado a la ruta que eligió. Esta ruta ruta no tiene cupos disponibles.")
    else:
        print("No se encontró el camper con el id que ingresó.")
elif opc=="4":
    id=int(input("Ingrese el id del nuevo trainer: "))
    nombre=input("Ingrese el nombre del nuevo trainer: ")
    ruta=input("Ingrese la ruta del nuevo trainer: ")
    horario=input("Ingrese el horario del nuevo trainer: ")
    print("El nuevo trainer fue registrado exitosamente")
elif opc=="5":
    nombreTrainer=input("Ingrese el nombre del trainer: ")
    trainer=next((trainer for trainer in trainers.trainers if trainer.nombre==nombreTrainer), None)
    if trainer:
        rutaNombre=input("Ingrese el nombre de la ruta: ")
        if reporte.rutaTrainers(trainer, rutaNombre):
            print("La ruta fue asignada al trainer")
        else:
            print("No se encontró la ruta")
    else:
        print("No se encontró el trainer con ese nombre")
elif opc=="6":
    reporte.campersInscritos()
elif opc=="7":
    reporte.reporteCampersAprobados()
elif opc=="8":
    reporte.reporteTrainersTrabajando()
elif opc =="9":
    print("Hasta luego. Vuelve pronto")
else: 
    print("Esta opción no existe. Por favor ingrese otra")

'''
while True:
    print("")
    print("----------BIENVENIDOS---------")
    print("")
    print("---------MENÚ----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Coordinador")
    print("4. Salir")
    opc=input("Elije una de nuestras opciones: ")
    miInfo=[]
    mijson = abrirarchivo()
    if opc ==1:
        print("")
    usuario=int(input("Ingrese su número de identificación: "))
    print("")
    contraseña = input("Ingrese su contraseña: ")
    print("")
    for i in mijson:
        for usuario in i["campers"]:
            if usuario ["id"] == usuario:
                if "contraseña" in usuario and usuario["contraseña"] == contraseña:
                    print("Inicio de sesión exitoso", usuario["nombre"])
    print("")

    if opc ==2:

#######################

        print("-----------MENÚ----------")
        print("1. Subir datos del camper")
        print("2. Datos nuevos del camper")
        print("3. Campers nuevos")
        print("4. Inscripción de campers")
        print("5. Estado de los campers")
        print("6. Campers aprobados")
        print("7. Matriculas nuevas de los campers")
        print("8. Campers con bajo rendimiento")
        print("9. Rendimiento calculado")
        print("10. Ruta de los trainers")
        print("11. Campers ruta")
        print("12. Trainers trabajando")
        print("13. Módulo de los campers")
        print("14. Reportes")
        print("15. Salir")
        x=input("Seleccione una opción: ")
        miInfo=[]
    if x == "1":
        miInfo=abrirarchivo()
        camperID= input("Ingrese el id del camper: ")
        nombre= input("Ingrese el nombre del camper: ")
        apellido= input("Ingrese el apellido del camper: ")
        direccion= input("Ingrese la dirección del camper: ")
        acudiente= input("Ingrese el nombre y el apellido de el acudiente del camper: ")
        numero_celular= input("Ingrese el número de teléfono del camper: ")
        numero_fijo= input("Ingrese el número fijo del camper: ")
        estado= input("Ingrese el estado del camper: ")
        riesgo= input("Ingrese el riesgo del camper: ")
        camperNuevo = campers(id, nombre, apellido, direccion, acudiente, numero_celular, numero_fijo, estado, riesgo)
        inscripcion(camperNuevo, "campus.json")
        print("El camper fue inscrito satisfactoriamente.\n")

    elif x == "2":
        miInfo=abrirarchivo()
        datos= input("Ingrese los datos nuevos(inscrito, aprobado, cursando, graduado, en proceso de ingreso, expulsado, retirado)")
        datosNuevos=campers(estado, "campus.json")

    elif x =="3":
        nuevos= input("Ingrese el nuevo nombre del camper: ")
        camperNuevo= campers(nuevos, "campus.json")

    elif x =="4":
        inscritos= input("Los campers inscritos son: ")
        inscripcion=campers(inscritos, "campus.json")

    elif x =="5":
        estados=input("Los campers por estados son: ")
        estadoCampers=campers(estados, "campus.json")

    elif x =="6":
        aprobados= input("Los campers aprobados son: ")
        campersAprobados=(aprobados, "campus.json")

    elif x =="7":
        matriculas= input("Nuevas matriculas: ")
        matriculaNueva=(matriculas, "campus.json")

    elif x =="8":
        rendimiento= input("Rendimiento de los campers: ")
        campersRendimientoBajo=(rendimiento, "campus.json")
        
    elif x =="9":
        calculado= input("Rendimiento calculado de los campers: ")
        rendimientoCalculado=(calculado, "campus.json")

    elif x =="10":
        trainerRuta= input("Ruta de los trainers: ")
        campersTrainerRuta=(trainerRuta, "campus.json")

    elif x =="11":
        estadoRuta= input("Estado de los campers en la ruta: ")
        campersEstadoRuta=(estadoRuta, "campus.json")

    elif x =="12":
        trabajando= input("Trainers que se encuentran laborando: ")
        trainersTrabajando=(trabajando, "campus.json")

    elif x =="13":
        moduloRuta= input("Modulos disponibles para los campers: ")
        campersModuloRuta=(moduloRuta, "campus.json")

    elif x =="14":
        reportesCampers= input("Reporte de los campers: ")
        reporte=(reportesCampers, "campus.json")

    elif x =="15":
        print("Saliendo del programa")
        print("Saliendo..............")
        print("Has salido exitosamente del programa")
        
    else:
        print("Esta opción no existe, por favor elige otra: ")



            
            


'''

