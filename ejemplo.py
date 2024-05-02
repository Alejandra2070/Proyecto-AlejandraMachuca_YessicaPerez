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
    def __init__(self, id, nombre, ruta, horario):
        self.id=id
        self.nombre=nombre
        self.ruta=ruta
        self.horario=horario
class ruta:
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
class coordinador:
    def __init__(self, id, nombre, apellido, cargo):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.cargo=cargo