from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorio_participante import RepositorioParticipante
from modelos.entidades.participante import Participante

participante_bp = Blueprint('participante', __name__)
repositorio_participante = RepositorioParticipante()

@participante_bp.route('/participantes', methods=['GET'])
def obtener_participantes():
    return jsonify(repositorio_participante.obtener_todos())

@participante_bp.route('/participantes/<int:id>', methods=['GET'])
def obtener_participante(id):
    participante = repositorio_participante.obtener_participante(id)
    if participante:
        return jsonify(participante.to_dict())
    return jsonify({"error": "Participante no encontrado"}), 404

@participante_bp.route('/participantes', methods=['POST'])
def crear_participante():
    if not request.is_json:
        return jsonify({"mensaje": "Los datos deben estar en formato JSON."}), 400

    datos = request.json
    required_fields = ["id", "nombre", "apellido", "email"]
    for field in required_fields:
        if field not in datos:
            return jsonify({"error": f"Falta el campo requerido: {field}"}), 400

    nuevo_participante = Participante(datos["id"], datos["nombre"], datos["apellido"], datos["email"])

    if repositorio_participante.existe_participante(nuevo_participante.obtener_nombre()):
        return jsonify({"mensaje": "El participante con este nombre ya existe."}), 400

    try:
        repositorio_participante.agregar_participante(nuevo_participante)
        return jsonify({"mensaje": "Participante agregado con éxito.", "participante": nuevo_participante.to_dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@participante_bp.route('/participantes/<int:id>', methods=['PUT'])
def actualizar_participante(id):
    if not request.is_json:
        return jsonify({"mensaje": "Los datos deben estar en formato JSON."}), 400

    datos = request.json
    required_keys = ["nombre", "apellido", "email"]
    for key in required_keys:
        if key not in datos:
            return jsonify({"error": f"Falta el campo requerido: {key}"}), 400

    participante = Participante(id, datos["nombre"], datos["apellido"], datos["email"])
    if repositorio_participante.actualizar_participante(id, participante):
        return jsonify(participante.to_dict())
    return jsonify({"error": "Participante no encontrado"}), 404

@participante_bp.route('/participantes/<int:id>', methods=['DELETE'])
def eliminar_participante(id):
    if repositorio_participante.eliminar_participante(id):
        return jsonify({"mensaje": "Participante eliminado"})
    return jsonify({"error": "Participante no encontrado"}), 404
