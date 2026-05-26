print("ESTE ES MI APP CORRECTO")

from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LIMAPO",
    database="herbalife_db"
)

#LOGIN
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    
    print("Correo recibido:", correo)
    print("Contraseña recibida:", contrasena)

    cursor = conexion.cursor(dictionary=True)
    
    query = "SELECT * FROM usuario WHERE correoElectronico=%s"
    cursor.execute(query, (correo,))
    usuario = cursor.fetchone()

    print("Usuario encontrado:", usuario)
    
    if usuario:
        print("Hash en BD:", usuario['contrasena'])
        print("Contraseña ingresada:", contrasena)
        
        resultado = check_password_hash(usuario['contrasena'], contrasena)
        print("Resultado:", resultado)
        
        if resultado:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    else:
        return jsonify({"success": False})

# REGISTRO
@app.route('/api/registro', methods=['POST'])
def registro():
    data = request.get_json()

    nombre = data.get('nombreApellido')
    correo = data.get('correoElectronico')
    contrasena = data.get('contrasena')
    telefono = data.get('telefono')

    print("Registrando usuario:", correo)

    hash_password = generate_password_hash(contrasena)

    cursor = conexion.cursor()

    query = """
    INSERT INTO usuario
    (nombreApellido, correoElectronico, contrasena, telefono)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (nombre, correo, hash_password, telefono))
    conexion.commit()

    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(port=3000, debug=True)