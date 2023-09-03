from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='favorites')
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    character = db.relationship('Characters', backref='favorited_by')
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    planet = db.relationship('Planets', backref='favorited_by', foreign_keys=[planet_id])
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)
    vehicle = db.relationship('Vehicle', backref='favorited_by')
    film_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=True)
    film = db.relationship('Films', backref='favorited_by')
    
    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id_favorito": self.id,
            "usuario": self.user_id,
            "vehiculo_id": self.vehicle_id,
            "planet_id": self.planet_id,
            "film_id": self.film_id,
            "character_id": self.character_id

            # do not serialize the password, its a security breach
        }
    
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), unique=True, nullable=False)
    Height = db.Column(db.String(80), unique=False, nullable=False)
    Mass = db.Column(db.String(80), unique=False, nullable=False)
    Hair_Color = db.Column(db.String(80), unique=False, nullable=False)
    Skin_Color = db.Column(db.String(80), unique=False, nullable=False)
    Eye_Color = db.Column(db.String(80), unique=False, nullable=False)
    Birth_Year = db.Column(db.String(80), unique=False, nullable=False)
    Gender = db.Column(db.String(80), unique=False, nullable=False)
    
    
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "Height": self.Height,
            "Mass": self.Mass,
            "Hair_Color": self.Hair_Color,
            "Skin_Color": self.Skin_Color,
            "Eye_Color": self.Eye_Color,
            "Birth_Year": self.Birth_Year,
            "Gender": self.Gender,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    surface_water = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }                 


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Modelo = db.Column(db.String(120), unique=True, nullable=False)
    Manufacturer = db.Column(db.String(80), unique=False, nullable=False)
    Cost_in_credits = db.Column(db.String(80), unique=False, nullable=False)
    Lenght = db.Column(db.String(80), unique=False, nullable=False)
    Max_Speed = db.Column(db.String(80), unique=False, nullable=False)
    Crew = db.Column(db.String(80), unique=False, nullable=False)
    Passengers = db.Column(db.String(80), unique=False, nullable=False)
    
    
    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Modelo": self.Modelo,
            "Manufacturer": self.Manufacturer,
            "Cost_in_credits": self.Cost_in_credits,
            "Lenght": self.Lenght,
            "Max_Speed": self.Max_Speed,
            "Crew": self.Crew,
            "Passengers": self.Passengers, 
        }
    
class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(120), unique=True, nullable=False)
    Director = db.Column(db.String(80), unique=False, nullable=False)
    Produccion = db.Column(db.String(80), unique=False, nullable=False)
    Fecha_de_Estreno = db.Column(db.String(80), unique=False, nullable=False)
    
    
    
    def __repr__(self):
        return '<Films %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Title": self.Title,
            "Director": self.Director,
            "Prodcuccion": self.Produccion,
            "Fecha_de_Estreno": self.Fecha_de_Estreno,
          
        }