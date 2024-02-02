from bayeta import frotar, insertar_frases
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def hola_mundo(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    try:
        # Obtener el JSON del cuerpo de la solicitud
        datos_json = request.get_json()

        # Verificar si 'frases' está presente en el JSON
        if 'frases' in datos_json:
            nuevas_frases = datos_json['frases']

            # Llamar a la función de inserción en bayeta.py
            insertar_frases(nuevas_frases)

            # Devolver código de respuesta 200
            return jsonify({"message": "Frases añadidas exitosamente"}), 200
        else:
            # Devolver código de respuesta 400 si 'frases' no está presente
            return jsonify({"error": "El JSON debe contener una clave 'frases'"}), 400

    except Exception as e:
        # Devolver código de respuesta 500 en caso de error
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
