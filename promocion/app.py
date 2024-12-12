from flask import Flask
from rutas.rutas_evento import evento_bp
from rutas.rutas_localizacion import localizacion_bp
from rutas.rutas_participante import participante_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(evento_bp)
app.register_blueprint(localizacion_bp)
app.register_blueprint(participante_bp)

if __name__ == '__main__':
    app.run(debug=True)
