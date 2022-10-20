from Modelos.Inscripcion import Inscripcion
from Repositorios.RepositorioInscripcion import RepositorioInscripcion

class ControladorInscripcion():
    def __init__(self):
        print("Creando ControladorInscripcion")
        self.repositorioInscripcion = RepositorioInscripcion()
    def index(self):
        print("Listar todas las inscripciones")
        return RepositorioInscripcion.findAll()
    def create(self,infoInscripcion):
        print("Crear una inscripcion")
        nuevaInscripcion=Inscripcion(infoInscripcion)
        return self.repositorioInscripcion.save(nuevaInscripcion)
    def show(self,id):
        print("Mostrando una inscripcion con id ",id)
        laInscripcion=Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__
    def update(self,id,infoInscripcion):
        print("Actualizando inscripcion con id ",id)
        inscripcionActual=Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcionActual.id=infoInscripcion["id"]
        inscripcionActual.anio = infoInscripcion["año"]
        inscripcionActual.semestre = infoInscripcion["semestre"]
        inscripcionActual.nota_final = infoInscripcion["nota_final"]
        return self.repositorioInscripcion.save(inscripcionActual)
    def delete(self,id):
        print("Elimiando inscripcion con id ",id)
        return self.repositorioInscripcion.delete(id)