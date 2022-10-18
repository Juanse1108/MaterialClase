from Modelos.Inscripcion import Inscripcion

class ControladorInscripcion():
    def __init__(self):
        print("Creando ControladorInscripcion")

    def index(self):
        print("Listar todas las inscripciones")
        unaInscripcion={"_id":"abc123",
                        "año":"2022",
                        "semestre":"4",
                        "nota_final":"4.5"
                        }
        return [unaInscripcion]

    def create(self,infoInscripcion):
        print("Crear una inscripcion")
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def show(self,id):
        print("Mostrando una inscripcion con id ",id)
        laInscripcion = {"_id": id,
                        "año":"2022",
                        "semestre":"4",
                        "nota_final":"4.5"
                        }
        return laInscripcion

    def update(self,id,infoInscripcion):
        print("Actualizando inscripcion con id ",id)
        laInscripcion = Inscripcion(infoInscripcion)
        return laInscripcion.__dict__

    def delete(self,id):
        print("Elimiando inscripcion con id ",id)
        return {"deleted_count":1}