from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorio_evento import RepositorioEvento
from modelos.entidades.evento import Evento

evento_bp = Blueprint('evento', __name__)
repositorio_evento = RepositorioEvento()

@evento_bp.route('/eventos', methods=['GET'])
def obtener_eventos():
    return jsonify(repositorio_evento.obtener_todos())

@evento_bp.route('/eventos/<int:id>', methods=['GET'])
def obtener_evento(id):
    evento = repositorio_evento.obtener_evento(id)
    if evento:
        return jsonify(evento.to_dict())
    return jsonify({"error": "Evento no encontrado"}), 404

@evento_bp.route('/eventos', methods=['POST'])
def crear_evento():
    datos = request.json
    evento = Evento(datos["id"], datos["nombre"], datos["fecha"], datos["localizacion_id"])
    repositorio_evento.agregar_evento(evento)
    return jsonify(evento.to_dict()), 201

@evento_bp.route('/eventos/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    datos = request.json
    evento = Evento(id, datos["nombre"], datos["fecha"], datos["localizacion_id"])
    if repositorio_evento.actualizar_evento(id, evento):
        return jsonify(evento.to_dict())
    return jsonify({"error": "Evento no encontrado"}), 404

@evento_bp.route('/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    if repositorio_evento.eliminar_evento(id):
        return jsonify({"mensaje": "Evento eliminado"})
    return jsonify({"error": "Evento no encontrado"}), 404
