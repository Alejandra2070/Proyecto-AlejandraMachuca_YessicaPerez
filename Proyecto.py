import json
archivo_json = "campus.json"
with open(archivo_json, encoding="utf-8")as file:
    datos_json = json.load(file)
print(datos_json)

def menu():
    while True:

        print("-----------MENÚ----------")
        print("1. Campers")
        print("2. Rutas de entrenamiento")
        print("3. Trainers")
        print("4. Matricular campers")
        print("5. Coordinador")
        print("6. Asignar trainers")
        print("7. Evaluar modulo")
        print("8. Reportes")
        print("9. Salir")
        opc=input("Seleccione una opción: ")
        if opc == "1":
           campers()
        elif opc =="2":
            ruta()
        elif opc =="3":
            trainers()
        elif opc =="4":
            matricula()
        elif opc =="5":
            coordinador()
        elif opc =="6":
            trainersTrabajando()
        elif opc =="7":
            campersModuloRuta()
        elif opc =="8":
            reportes()
        elif opc =="9":
            print("Saliendo del programa")
            break
        else:
            print("Esta opción no existe, por favor elige otra: ")

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
class trainers:
    def __init__(self, id, nombre, ruta, horario):
        self.id=id
        self.nombre=nombre
        self.ruta=ruta
        self.horario=horario
class ruta:
    def __init__(self, nombre, modulos, SGSB_principal, SGDB_alternativo, capacidad_maxima):
        self.nombre=nombre
        self.modulos=modulos
        self.SGDB_principal=SGSB_principal
        self.SGDB_alternativo=SGDB_alternativo
        self.capacidad_maxima=capacidad_maxima
class matricula:
    def __init__(self, campersID, rutaNombre, fechaI, fechaF, salon):
        self.campersID=campersID
        self.rutaNombre=rutaNombre
        self.fechaI=fechaI
        self.fechaF=fechaF
        self.salon=salon
class coordinador:
    def __init__(self, id, nombre, apellido, cargo):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo
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
    datosNuevos(camper, nombreArchivo)
def inscripcion(camper, nombreArchivo):
  camperNuevo(camper, nombreArchivo)
def estadoCampers(estado, nombreArchivo):
    camper=subirDatos(nombreArchivo)
    return[camper(camper)for camper in campers if camper["estado"]==estado]
def campersAprobados(nombreArchivo):
 campers=subirDatos(nombreArchivo)
 return[camper(camper)for camper in campers if camper ["estado"]=="aprobado"]
def matriculaNueva(matricula, nombreArchivo):
    matriculas=subirDatos(nombreArchivo)
    matriculas.append(matricula.__dict__)
    datosNuevos(matriculas, nombreArchivo)
def campersRendimientoBajo(matriculasArchivo, campersArchivo):
    matriculas=subirDatos(matriculasArchivo)
    campers=subirDatos(campersArchivo)
    campersRendimientoBajo=[]
    for matricula in matriculas:
        camper=next((camper for camper in campers if camper["id"]==matricula["camperID"]), None)
        if camper:
            rendimiento=rendimientoCalculado(matricula)
            if rendimiento<60:
                campersRendimientoBajo.append(camper(camper))
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
def menu():
    while True:
        print("-----------MENÚ----------")
        print("1. Campers")
        print("2. Rutas de entrenamiento")
        print("3. Trainers")
        print("4. Matricular campers")
        print("5. Coordinador")
        print("6. Asignar trainers")
        print("7. Evaluar modulo")
        print("8. Reportes")
        print("9. Salir")
        opc=input("Seleccione una opción: ")
        if opc == "1":
           campers()
        elif opc =="2":
            ruta()
        elif opc =="3":
            trainers()
        elif opc =="4":
            matricula()
        elif opc =="5":
            coordinador()
        elif opc =="6":
            trainersTrabajando()
        elif opc =="7":
            campersModuloRuta()
        elif opc =="8":
            reportes()
        elif opc =="9":
            print("Saliendo del programa")
            break
        else:
            print("Esta opción no existe, por favor elige otra: ")


        
        

