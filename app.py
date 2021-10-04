# Import necessary modules
from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from os.path import join, dirname
from Controllers.PokemonController import PokemonController
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

# Setup dotenv
dotenvPath = join(dirname(__file__), '.env')
load_dotenv(dotenvPath)

# Config variables
DEBUG_MODE = bool(os.getenv('DEBUG_MODE'))
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABSE_PORT = int(os.environ.get("DATABSE_PORT"))
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

# Setup database connection
databaseUri = "mysql+pymysql://" + DATABASE_USER + ":" + DATABASE_PASSWORD + "@" + DATABASE_HOST + ":" + str(DATABSE_PORT) + "/" + DATABASE_NAME
dbConnection = create_engine(databaseUri)

# Set up the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseUri
db = SQLAlchemy(app)

# Define database models
class Pokemon(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text)
    Type1 = db.Column('Type 1', db.Text)
    Type2 = db.Column('Type 2', db.Text)
    Total = db.Column(db.Text)
    HP = db.Column(db.Integer)
    Attack = db.Column(db.Integer)
    Defense = db.Column(db.Integer)
    SpAtk = db.Column('Sp. Atk', db.Integer)
    SpDef = db.Column('Sp. Def', db.Integer)
    Speed = db.Column(db.Integer)
    Generation = db.Column(db.Integer)
    Legendary = db.Column(db.Integer)

    def __repr__(self) :
        return "{} is the title and {} is the description".format(self.title,self.description)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "Attack": self.Attack,
            "Defense":  self.Defense,
            "Generation": self.Generation,
            "HP": self.HP,
            "Legendary": self.Legendary,
            "Name": self.Name,
            "Sp. Atk": self.SpAtk,
            "Sp. Def": self.SpDef,
            "Speed": self.Speed,
            "Total": self.Total,
            "Type 1": self.Type1,
            "Type 2": self.Type2
        }

# Set up the controllers
pokemonController = PokemonController(dbConnection, Pokemon)

# Create route to get all pokemons from the database
@app.route('/database/pokemons')
def getAllPokemons():
    data = pokemonController.getAllFromDatabase()
    return jsonify(data)

# Create route to get all pokemons from the csv
@app.route('/csv/pokemons')
def getAllPokemonsFromCsv():
    data = pokemonController.getAllFromCsv()
    return jsonify(data)

# Create route to get export pokemons from the database
@app.route('/database/pokemons/import')
def importAllPokemonsToDatabase():
    data = pokemonController.importAllToDatabase()
    return jsonify(data)

# Start the server
if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)
