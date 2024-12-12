class RepositorioLocalizacion:
    def __init__(self):
        self.__localizaciones = {}

    def agregar_localizacion(self, localizacion):
        self.__localizaciones[localizacion.to_dict()["id"]] = localizacion

    def obtener_localizacion(self, id):
        return self.__localizaciones.get(id)

    def obtener_todos(self):
        return [localizacion.to_dict() for localizacion in self.__localizaciones.values()]

    def actualizar_localizacion(self, id, localizacion):
        if id in self.__localizaciones:
            self.__localizaciones[id] = localizacion
            return True
        return False

    def eliminar_localizacion(self, id):
        if id in self.__localizaciones:
            del self.__localizaciones[id]
            return True
        return False
