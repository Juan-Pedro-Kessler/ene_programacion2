class Participante:
    @classmethod
    def fromDiccionario(cls, data: dict) -> "Participante":
        if not isinstance(data, dict):
            raise ValueError("El parámetro data debe ser un diccionario.")
        return cls(data["id"], data["nombre"], data["apellido"], data["email"])
    def __init__(self, id, nombre, apellido, email):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
        }
    def obtener_nombre(self):
        return self.__nombre