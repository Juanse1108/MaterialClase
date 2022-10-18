from Modelos.Departamento import Departamento

class ControladorDepartamento():
    def __init__(self):
        print("Creando ControladorDepartamento")

    def index(self):
        print("Listar todos los departamentos")
        unDepartamento={"_id":"abc123",
                      "nombre":"Ciencias Basicas",
                      "Descripcion":"Algo"
                      }
        return [unDepartamento]

    def create(self,infoDepartamento):
        print("Crear un departamento")
        elDepartamento = Departamento(infoDepartamento)
        return elDepartamento.__dict__

    def show(self,id):
        print("Mostrando un departamento con id ",id)
        elDepartamento={"_id":id,
                      "nombre":"Ciencias Basicas",
                      "Descripcion":"Algo"
                      }
        return elDepartamento

    def update(self,id,infoDepartamento):
        print("Actualizando departamento con id ",id)
        elDepartamento = Departamento(infoDepartamento)
        return elDepartamento.__dict__

    def delete(self,id):
        print("Elimiando departamento con id ",id)
        return {"deleted_count":1}