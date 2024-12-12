from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorio_localizacion import RepositorioLocalizacion
from modelos.entidades.localizacion import Localizacion

localizacion_bp = Blueprint('localizacion', __name__)
repositorio_localizacion = RepositorioLocalizacion()

@localizacion_bp.route('/localizaciones', methods=['GET'])
def obtener_localizaciones():
    return jsonify(repositorio_localizacion.obtener_todos())

@localizacion_bp.route('/localizaciones/<int:id>', methods=['GET'])
def obtener_localizacion(id):
    localizacion = repositorio_localizacion.obtener_localizacion(id)
    if localizacion:
        return jsonify(localizacion.to_dict())
    return jsonify({"error": "Localización no encontrada"}), 404

@localizacion_bp.route('/localizaciones', methods=['POST'])
def crear_localizacion():
    datos = request.json
    localizacion = Localizacion(datos["id"], datos["nombre"], datos["direccion"])
    repositorio_localizacion.agregar_localizacion(localizacion)
    return jsonify(localizacion.to_dict()), 201

@localizacion_bp.route('/localizaciones/<int:id>', methods=['PUT'])
def actualizar_localizacion(id):
    datos = request.json
    localizacion = Localizacion(id, datos["nombre"], datos["direccion"])
    if repositorio_localizacion.actualizar_localizacion(id, localizacion):
        return jsonify(localizacion.to_dict())
    return jsonify({"error": "Localización no encontrada"}), 404

@localizacion_bp.route('/localizaciones/<int:id>', methods=['DELETE'])
def eliminar_localizacion(id):
    if repositorio_localizacion.eliminar_localizacion(id):
        return jsonify({"mensaje": "Localización eliminada"})
    return jsonify({"error": "Localización no encontrada"}), 404
