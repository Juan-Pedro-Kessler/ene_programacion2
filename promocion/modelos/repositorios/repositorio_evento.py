class RepositorioEvento:
    def __init__(self):
        self.__eventos = {}

    def agregar_evento(self, evento):
        self.__eventos[evento.to_dict()["id"]] = evento

    def obtener_evento(self, id):
        return self.__eventos.get(id)

    def obtener_todos(self):
        return [evento.to_dict() for evento in self.__eventos.values()]

    def actualizar_evento(self, id, evento):
        if id in self.__eventos:
            self.__eventos[id] = evento
            return True
        return False

    def eliminar_evento(self, id):
        if id in self.__eventos:
            del self.__eventos[id]
            return True
        return False
