class Localizacion:
    
    @classmethod
    def fromDiccionario(cls, data: dict) -> "Localizacion":
        if not isinstance(data, dict):
            raise ValueError("El parámetro data debe ser un diccionario.")
        return cls(data["id"], data["nombre"], data["direccion"])
    def __init__(self, id, nombre, direccion):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "direccion": self.__direccion,
        }
