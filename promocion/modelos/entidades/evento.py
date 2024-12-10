class Evento:
    def __init__(self, id, nombre, fecha, localizacion_id):
        self.__id = id
        self.__nombre = nombre
        self.__fecha = fecha
        self.__localizacion_id = localizacion_id

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "fecha": self.__fecha,
            "localizacion_id": self.__localizacion_id,
        }
