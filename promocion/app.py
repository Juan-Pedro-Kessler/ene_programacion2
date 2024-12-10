from flask import Flask
from rutas.rutas_alumnos import bp_alumnos
from rutas.rutas_deportes import bp_deportes

app = Flask(__name__)

app.register_blueprint(bp_alumnos)
app.register_blueprint(bp_deportes)

if __name__ == '__main__':
    app.run(debug=True)
