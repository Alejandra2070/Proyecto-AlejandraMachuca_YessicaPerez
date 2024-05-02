import json
def abrirarchivo():
    mijson=[]
    with open("campus.json","r") as openfile:
        mijson=json.load(openfile)
    return mijson

print("")
print("----------BIENVENIDOS---------")
print("")

class campers:
    def __init__(self, id, nombre, apellido, direccion, acudiente, numero_celular, numero_fijo, estado, riesgo):
        self.id=id
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
class rutaEntrenamiento:
    def __init__(self, nombre, modulos, SGDB_principal, SGDB_alternativo, capacidad_maxima):
        self.nombre=nombre
        self.modulos=modulos
        self.SGDB_principal=SGDB_principal
        self.SGDB_alternativo=SGDB_alternativo
        self.capacidad_maxima=capacidad_maxima
class matricula:
    def __init__(self, campersID, rutaNombre, fechaI, fechaF, salon):
        self.campersID=campersID
        self.rutaNombre=rutaNombre
        self.fechaI=fechaI
        self.fechaF=fechaF
        self.salon=salon
    def asignarCamper(self, campers, ruta, fechaI, fechaF, salon):
        if ruta.asignarCamper(campers):
            print(f"Camper {campers.nombre} fue asignado a la ruta {ruta.nombre}")
        else:
            print("No existen cupos disponibles para esta ruta")
class coordinador:
    def __init__(self, id, nombre, apellido, cargo):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo
    def subirNota(self, campers, notaTeorica, notaPractica):
        promedio=(notaTeorica+notaPractica)/2
        if promedio>=60:
            campers.estado="aprobado"
            print(f"Nota registrada{campers.nombre}:teorica:{notaTeorica},practica:{notaPractica}aprobado")
        else:
            print(f"Nota registrada{campers.nombre}:teorica:{notaTeorica},practica:{notaPractica}no aprobado")
class reporte:
    def __init__(self, id, rutaEntrenamiento, campersInscritos):
        self.id=id
        self.rutaEntrenamiento=rutaEntrenamiento
        self.campersInscritos=campersInscritos
    def listarCampersInscritos(self, rutaEntrenamiento):
        print(f"Campers inscritos en la ruta de entrenamiento {rutaEntrenamiento.nombre}")
        print(rutaEntrenamiento.listarCampers())
def subirDatos(nombreArchivo):
    try:
        with open(nombreArchivo, "r") as file:
         return json.load(file)
    except FileNotFoundError:
        return []
def datosNuevos(datos, nombreArchivo):
    with open(nombreArchivo, "w")as file:
        json.dump(datos, file)
def camperNuevo(camper, nombreArchivo):
    camper=subirDatos(nombreArchivo)
    camper.append(camper.__dict__)
    datosNuevos(campers, nombreArchivo)
def inscripcion(campers, nombreArchivo):
  camperNuevo(campers, nombreArchivo)
def estadoCampers(estado, nombreArchivo):
    camper=subirDatos(nombreArchivo)
    return[camper(campers)for camper in campers if campers["estado"]==estado]
def campersAprobados(nombreArchivo):
 campers=subirDatos(nombreArchivo)
 return[camper(campers)for camper in campers if campers["estado"]=="aprobado"]
def matriculaNueva(matricula, nombreArchivo):
    matriculas=subirDatos(nombreArchivo)
    matriculas.append(matricula.__dict__)
    datosNuevos(matriculas, nombreArchivo)
def campersRendimientoBajo(matriculasArchivo, campersArchivo):
    matriculas=subirDatos(matriculasArchivo)
    camper=subirDatos(campersArchivo)
    campersRendimientoBajo=[]
    for matricula in matriculas:
        camper=next((camper for camper in campers if campers["id"]==matricula["camperID"]), None)
        if camper:
            rendimiento=rendimientoCalculado(matricula)
            if rendimiento<60:
                campersRendimientoBajo.append(camper(campers))
    return campersRendimientoBajo
def rendimientoCalculado (matricula):
    return 55
def campersTrainerRuta(rutaNombre, trainersArchivo, matriculasArchivo):
    matriculas=subirDatos(matriculasArchivo)
    trainers=subirDatos(trainersArchivo)
    campersTrainers=[]
    for matricula in matriculas:
        if matricula["rutaNombre"]==rutaNombre:
            camperID=matricula["camperID"]
            trainer=next((trainer for trainer in trainers if trainer["ruta"]== rutaNombre), None)
            camper=next((camper for camper in campers if camper ["id"]==camperID), None)
            if trainer:
                campersTrainers.append((camper(camper),trainer(trainer)))
    return campersTrainers
def campersEstadoRuta(estado, rutaNombre, matriculasArchivo, campersArchivo):
    matriculas=subirDatos(matriculasArchivo)
    campers=subirDatos(campersArchivo)
    campersEstadoRuta=[]
    for matricula in matriculas:
        if matricula["rutaNombre"]==rutaNombre:
            camperID=matricula["camperID"]
            camper=next((camper for camper in campers if camper["id"]==camperID and camper["estado"]==estado),None)
            if camper:
                campersEstadoRuta.append(camper(camper))
    return campersEstadoRuta
def trainersTrabajando(trainersArchivo):
    trainers=subirDatos(trainersArchivo)
    return[trainers(trainers) for trainers in trainers]
def campersModuloRuta(modulo, rutaNombre, matriculasArchivo, campersArchivo):
    matriculas=subirDatos(matriculasArchivo)
    camper=subirDatos(campersArchivo)
    campersModuloRuta=[]
    for matricula in matriculas:
        if matricula["rutaNombre"]==rutaNombre:
            camperID=matricula["camperID"]
            camper=next((camper for camper in campers if camper ["id"]==camperID),None)
            if camper:
                campersModuloRuta.append(camper(camper))
    return campersModuloRuta
def reportes():
    inscripcion=estadoCampers("inscrito", "campers.json")
    campersAprobados=campersAprobados("campers.json")
    trainersTrabajando=trainersTrabajando("trainers.json")
    campersRendimientoBajo=campersRendimientoBajo("matricula.json", "campers.json")
    campersTrainerRuta=campersTrainerRuta("Ruta Java","trainers.json","matricula.json")
    campersModuloRuta=campersModuloRuta("programacionWeb","Ruta Java", "matricula.json", "campers.json")
    print("Campers inscritos: ")
    for camper in inscripcion:
        print(f"{camper.nombre}{camper.apellido}")
        print("\nCampers aprobados: ")
        for camper in campersAprobados:
            print(f"{camper.nombre}{camper.apellido}")
            print("\nTrainers trabajando: ")
            for trainer in trainersTrabajando:
                print(f"{trainer.nombre}")
                print("\nCampers con rendimiento bajo: ")
                for camper in campersRendimientoBajo:
                    print(f"{camper.nombre}{camper.apellido}")
                    print("\nCampers y trainers por ruta: ")
                    for camper, trainer in campersTrainerRuta:
                        print(f"Camper: {camper.nombre}{camper.apellido}, Trainer: {trainer.nombre}")
                        print("\nCamper por modulo y ruta: ")
                        for camper in campersModuloRuta:
                            print(f"{camper.nombre}{camper.apellido}")

while True:

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
        reportes=(reportesCampers, "campus.json")

    elif x =="15":
        print("Saliendo del programa")
        print("Saliendo..............")
        print("Has salido exitosamente del programa")
        
    else:
        print("Esta opción no existe, por favor elige otra: ")



            
            

