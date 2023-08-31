"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Vehicle, Films, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# endpoints usuario

@app.route('/user', methods=['GET'])
def get_usuario():

    usuario_query = User.query.all()
    results = list(map(lambda item: item.serialize(),usuario_query))
    print(results)

    if results == []:
         return jsonify({"msg":"No hay usuarios "}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "estos son los usuarios",
        "results": results
    }

    return jsonify(response_body), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def obtener_usuario(user_id):
    un_usuario_query = User.query.filter_by(id=user_id).first()

    if un_usuario_query is None:
         return jsonify({"msg": "El usuario no existe"}), 404

    response_body = {
        "msg": "Usuario",
        "nombre_usuario": un_usuario_query.serialize()
    }

    return jsonify(response_body), 200



#Endoint para obtener los favoritos

@app.route('/favoritos', methods=['GET'])
def get_favoritos():

    get_favoritos_query = Favorite.query.all()


    results = list(map(lambda item: item.serialize(),get_favoritos_query))
    print(results)

    if results == []:
         return jsonify({"msg":"No hay favorito "}), 404


#Regresamos una respuesta con los resultados de la consulta

    response_body = {
        "msg": "Usuarios que agregaron favoritos",
        "results": results
    }

    return jsonify(response_body), 200

@app.route('/favoritos/<int:favorito_id>', methods=['GET'])
def favorito(favorito_id):
    favorito_query = Favorite.query.filter_by(id= favorito_id).first()

    print(favorito_query)

    if favorito_query is None:
         return jsonify({"msg":"lista vacia"}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Favoritos del usuario",
        "result": favorito_query.serialize()
    }

    return jsonify(response_body), 200

# endoint para obtener todos los Planetas

@app.route('/planetas', methods=['GET'])
def get_planetas():

#Consulta a la tabla planeta para que traiga todos los registros
    palents_query = Planets.query.all()

#Mapeo para converir el array [<Planetas 1>] => un array de objetos
    results = list(map(lambda item: item.serialize(),palents_query))
    print(results)

    if results == []:
         return jsonify({"msg":"No hay planetas "}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "estos son los planetas",
        "results": results
    }

    return jsonify(response_body), 200

@app.route('/planetas/<int:planet_id>', methods=['GET'])
def planeta1(planet_id):

    print(planet_id)
    planeta_query = Planets.query.filter_by(id= planet_id).first()
    print(planeta_query)

    if planeta_query is None:
         return jsonify({"msg":"El planeta no existe"}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "estos son los planetas",
        "result": planeta_query.serialize()
    }

    return jsonify(response_body), 200

#Endoint para obtener los personajes

@app.route('/personajes', methods=['GET'])
def get_personajes():

    personajes_query = Characters.query.all()

    results = list(map(lambda item: item.serialize(),personajes_query))
    print(results)

    if results == []:
         return jsonify({"msg":"No hay personajes"}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "estos son los personajes",
        "results": results
    }

    return jsonify(response_body), 200

@app.route('/personajes/<int:persona_id>', methods=['GET'])
def persona(persona_id):

    print(persona_id)
    persona_query = Characters.query.filter_by(id= persona_id).first()
    print(persona_query)

    if persona_query is None:
         return jsonify({"msg":"El personaje no existe"}), 404


#Regresamos una respuesta con los resultados de la consulta
    response_body = {
        "msg": "Personajes ",
        "result": persona_query.serialize()
    }

    return jsonify(response_body), 200


# Ruta para obtener todos los vehículos
@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    get_vehicles_query = Vehicle.query.all()

    results = list(map(lambda item: item.serialize(), get_vehicles_query))
    print(results)

    if results == []:
         return jsonify({"msg": "No hay vehiculos"}), 404

    response_body = {
        "msg": "estos son los vehiculos",
        "results": results
    }

    return jsonify(response_body), 200

# Ruta para obtener un vehículo específico por ID
@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def one_vehicle(vehicle_id):

    print(vehicle_id)
    one_vehicle_query = Vehicle.query.filter_by(id= vehicle_id).first()
    print(one_vehicle_query)

    if one_vehicle_query is None:
         return jsonify({"msg": "El vehiculo no existe"}), 404

    response_body = {
        "msg": "Vehiculo ",
        "results": one_vehicle_query.serialize()
    }

    return jsonify(response_body), 200 

# Ruta para obtener peliculas
@app.route('/peliculas', methods=['GET'])
def get_peliculas():

    get_peliculas_query = Films.query.all()

    results = list(map(lambda item: item.serialize(), get_peliculas_query))
    print(results)

    if results == []:
         return jsonify({"msg": "No hay peliculas"}), 404

    response_body = {
        "msg": "estas son las peliculas",
        "results": results
    }

    return jsonify(response_body), 200

# Ruta para obtener un vehículo específico por ID
@app.route('/peliculas/<int:pelicula_id>', methods=['GET'])
def one_pelicula(pelicula_id):

    print(pelicula_id)
    one_pelicula_query = Films.query.filter_by(id= pelicula_id).first()
    print(one_pelicula_query)

    if one_pelicula_query is None:
         return jsonify({"msg": "La pelicula no existe"}), 404

    response_body = {
        "msg": "Pelicula ",
        "results": one_pelicula_query.serialize()
    }

    return jsonify(response_body), 200 

#----------------------------------------------------------------------------------------

#[POST]
 
#Crear planeta 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
