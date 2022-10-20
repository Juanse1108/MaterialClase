from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Creando ControladorEstudiante")
        self.repositorioEstudiante = RepositorioEstudiante()
    def index(self):
        print("Listar todas los estudiantes")
        return self.repositorioEstudiante.findAll()
    def create(self,infoEstudiante):
        print("Crear un estudiante")
        nuevoEstudiante=Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)
    def show(self,id):
        print("Mostrando un estudiante con id ",id)
        elEstudiante=Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
    def update(self,id,infoEstudiante):
        print("Actualizando un estudiante con id ",id)
        estudianteActual=Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula=infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self,id):
        print("Elimiando estudiante con id ", id)
        return self.repositorioEstudiante.delete(id)