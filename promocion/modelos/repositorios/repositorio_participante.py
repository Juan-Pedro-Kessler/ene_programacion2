import json
from modelos.entidades.participante import Participante
class RepositorioParticipante:
    ruta_archivo="datos/participantes.json"
    def __init__(self):
        self.__participantes = []
        self.__cargarParticipante()
        
    def __cargarParticipante(self):
        try:
            with open(RepositorioParticipante.ruta_archivo, "r") as archivo:
                lista_dicc_participantes = json.load(archivo)
                for participante in lista_dicc_participantes:
                    self.__participantes.append(Participante.fromDiccionario(participante))
    
        except FileNotFoundError:
            print("No se encontró el archivo de participantes")
        except Exception as e:
            print("Error cargando los participantes del archivo.\n" + str(e))

    def existe_participante(self, nombre: str):
        """Retorna True si existe un participante con el nombre, False en caso contrario"""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string válido")
        return any(p.obtener_nombre() == nombre for p in self.__participantes.values())

    def __guardarParticipante(self):
        try:
            with open(RepositorioParticipante.ruta_archivo, "w") as archivo: 
                datos = []
                for participante in self.__participantes:
                    datos.append(participante.toDiccionario())
                json.dump(datos, archivo, indent=4)
        except Exception as e:
            print("Error guardando los participantes en el archivo.\n" + str(e))
    def agregar_participante(self, participante: "Participante") ->bool:
        if isinstance(participante, Participante):
            if not self.existe_participante(participante.obtener_nombre()):
                self.participante.append(participante)
                self.__guardarParticipante()
                return True
        return False

    def obtener_participante(self, id):
        return self.__participantes.get(id)

    def obtener_todos(self):
        return [participante.to_dict() for participante in self.__participantes.values()]

    def actualizar_participante(self, id, participante):
        if id in self.__participantes:
            self.__participantes[id] = participante
            return True
        return False

    def eliminar_participante(self, id):
        if id in self.__participantes:
            del self.__participantes[id]
            return True
        return False
