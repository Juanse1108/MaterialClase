from Modelos.Departamento import Departamento
from Repositorios.RepositorioMateria import RepositorioMateria
from Modelos.Materia import Materia

class ControladorMateria():
    def __init__(self):
        print("Creando ControladorMateria")
        self.repositorioMateria = RepositorioMateria()
    def index(self):
        print("Listar todas las materias")
        return self.repositorioMateria.findAll()
    def create(self,infoMateria):
        print("Crear una materia")
        nuevaMateria=Materia(infoMateria)
        return self.repositorioMateria.save(nuevaMateria)
    def show(self,id):
        print("Mostrando una materia con id ",id)
        laMateria=Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__#.__dict__ (convierte el resultado en un JSON)
    def update(self,id,infoMateria):
        print("Actualizando materia con id ",id)
        materiaActual=Materia(self.repositorioMateria.findById(id))
        materiaActual.id=infoMateria["id"]
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)
    def delete(self,id):
        print("Elimiando materia con id ",id)
        return self.repositorioMateria.delete(id)

    """
    Relación departamento y materia (1 a n)
    """
    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)