from Modelos.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento


class ControladorDepartamento():
    def __init__(self):
        print("Creando ControladorDepartamento")
        self.repositorioDepartamento = RepositorioDepartamento()
    def index(self):
        print("Listar todos los departamentos")
        return self.repositorioDepartamento.findAll()
    def create(self,infoDepartamento):
        print("Crear un departamento")
        nuevoDepartamento=Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)
    def show(self,id):
        print("Mostrando un departamento con id ",id)
        elDepartamento=Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__
    def update(self,id,infoDepartamento):
        print("Actualizando departamento con id ",id)
        departamentoActual=Departamento(self.repositorioDepartamento.findById(id))
        departamentoActual.id=infoDepartamento["id"]
        departamentoActual.nombre = infoDepartamento["nombre"]
        return self.repositorioDepartamento.save(departamentoActual)
    def delete(self,id):
        print("Elimiando departamento con id ",id)
        return self.repositorioDepartamento.delete(id)