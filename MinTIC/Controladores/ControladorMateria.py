from Modelos.Materia import Materia

class ControladorMateria():
    def __init__(self):
        print("Creando ControladorMateria")

    def index(self):
        print("Listar todas las materias")
        unaMateria={"_id":"abc123",
                      "nombre":"Matematicas",
                      "creditos":"5"
                      }
        return [unaMateria]

    def create(self,infoMateria):
        print("Crear una materia")
        laMateria = Materia(infoMateria)
        return laMateria.__dict__

    def show(self,id):
        print("Mostrando una materia con id ",id)
        laMateria={"_id":id,
                      "nombre":"Matematicas",
                      "creditos":"5"
                      }
        return laMateria

    def update(self,id,infoMateria):
        print("Actualizando materia con id ",id)
        laMateria = Materia(infoMateria)
        return laMateria.__dict__

    def delete(self,id):
        print("Elimiando materia con id ",id)
        return {"deleted_count":1}