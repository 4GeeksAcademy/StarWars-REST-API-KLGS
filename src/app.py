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
 
#Crear planeta 

@app.route('/planetas', methods=['POST'])
def create_planet():
    request_body = request.json
    print(request_body)

    planet_query = Planets.query.filter_by(climate=request_body["climate"], diameter=request_body["diameter"], gravity=request_body["gravity"], id=request_body["id"], name=request_body["name"], orbital_period=request_body["orbital_period"], population=request_body["population"], rotation_period=request_body["rotation_period"], surface_water=request_body["surface_water"], terrain=request_body["terrain"]).first()

    if planet_query is None:
        new_planet = Planets(climate=request_body["climate"], diameter=request_body["diameter"], gravity=request_body["gravity"], id=request_body["id"], name=request_body["name"], orbital_period=request_body["orbital_period"], population=request_body["population"], rotation_period=request_body["rotation_period"], surface_water=request_body["surface_water"], terrain=request_body["terrain"])
        db.session.add(new_planet)
        db.session.commit()

        response_body = {
            "msg": "Planeta creado"
        }
        return jsonify(response_body), 200
    else:
        
        return jsonify({"msg": "Planeta ya existente"}), 400
    
 #Eliminar planeta   
@app.route('/planetas/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet_to_delete = Planets.query.get(planet_id)

    if planet_to_delete is None:
        return jsonify({"msg": "El planeta no existe"}), 404

    db.session.delete(planet_to_delete)
    db.session.commit()

    response_body = {
        "msg": "Planeta eliminado"
    }

    return jsonify(response_body), 200

    
#Crear personaje

@app.route('/personajes', methods=['POST'])
def create_personaje():
    request_body = request.json
    personaje_query = Characters.query.filter_by(Birth_Year=request_body["Birth_Year"], Eye_Color=request_body["Eye_Color"], Gender=request_body["Gender"], Hair_Color=request_body["Hair_Color"], Height=request_body["Height"], Mass=request_body["Mass"], Name=request_body["Name"], Skin_Color=request_body["Skin_Color"], id=request_body["id"]).first()
    if personaje_query is None:
        new_personaje = Characters(Birth_Year=request_body["Birth_Year"], Eye_Color=request_body["Eye_Color"], Gender=request_body["Gender"], Hair_Color=request_body["Hair_Color"], Height=request_body["Height"], Mass=request_body["Mass"], Name=request_body["Name"], Skin_Color=request_body["Skin_Color"], id=request_body["id"])
        db.session.add(new_personaje)
        db.session.commit()

        response_body = {
            "msg": "Personaje creado"
        }
        return jsonify(response_body), 200
    else:
        
        return jsonify({"msg": "Personaje ya existente"}), 400
    
 #Eliminar personaje  

@app.route('/personajes/<int:persona_id>', methods=['DELETE'])
def delete_personaje(persona_id):
    persona_to_delete = Characters.query.get(persona_id)

    if persona_to_delete is None:
        return jsonify({"msg": "El personaje no existe"}), 404

    db.session.delete(persona_to_delete)
    db.session.commit()

    response_body = {
        "msg": "Personaje eliminado"
    }

    return jsonify(response_body), 200

#Crear Vehiculo

@app.route('/vehicles', methods=['POST'])
def create_vehiculo():
    request_body = request.json
    print(request_body)

    vehiculo_query = Vehicle.query.filter_by(Modelo=request_body["Modelo"], Manufacturer=request_body["Manufacturer"], Cost_in_credits=request_body["Cost_in_credits"], Lenght=request_body["Lenght"], Max_Speed=request_body["Max_Speed"], Crew=request_body["Crew"], Passengers=request_body["Passengers"]).first()
    if vehiculo_query is None:
        new_vehiculo = Vehicle(Modelo=request_body["Modelo"], Manufacturer=request_body["Manufacturer"], Cost_in_credits=request_body["Cost_in_credits"], Lenght=request_body["Lenght"], Max_Speed=request_body["Max_Speed"], Crew=request_body["Crew"], Passengers=request_body["Passengers"])
        db.session.add(new_vehiculo)
        db.session.commit()

        response_body = {
            "msg": "Vehiculo creado"
        }
        return jsonify(response_body), 200
    else:
        
        return jsonify({"msg": "Vehiculo ya existente"}), 400
    
 #Eliminar vehiculo  
@app.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
def delete_vehiculo(vehicle_id):
    vehiculo_to_delete = Vehicle.query.get(vehicle_id)

    if vehiculo_to_delete is None:
        return jsonify({"msg": "El Vehiculo no existe"}), 404

    db.session.delete(vehiculo_to_delete)
    db.session.commit()

    response_body = {
        "msg": "Vehiculo eliminado"
    }

    return jsonify(response_body), 200

#Crear peliculas
@app.route('/peliculas', methods=['POST'])
def create_peliculas():
    request_body = request.json
    print(request_body)

    pelicula_query = Films.query.filter_by(id=request_body["id"],Title=request_body["Title"], Director=request_body["Director"], Produccion=request_body["Produccion"], Fecha_de_Estreno=request_body["Fecha_de_Estreno"]).first()
    if pelicula_query is None:
        new_pelicula = Films(id=request_body["id"],Title=request_body["Title"], Director=request_body["Director"], Produccion=request_body["Produccion"], Fecha_de_Estreno=request_body["Fecha_de_Estreno"])
        db.session.add(new_pelicula)
        db.session.commit()

        response_body = {
            "msg": "Pelicula creada"
        }
        return jsonify(response_body), 200
    else:
        
        return jsonify({"msg": "Pelicula ya existente"}), 400
    
 #Eliminar pelicula
@app.route('/peliculas/<int:pelicula_id>', methods=['DELETE'])
def pelicula_vehiculo(pelicula_id):
    pelicula_to_delete = Films.query.get(pelicula_id)

    if pelicula_to_delete is None:
        return jsonify({"msg": "La pelicula no existe"}), 404

    db.session.delete(pelicula_to_delete)
    db.session.commit()

    response_body = {
        "msg": "Pelicula eliminada"
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
