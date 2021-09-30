# Import necessary modules
from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from os.path import join, dirname
from Controllers.PokemonController import PokemonController
from sqlalchemy import create_engine

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

# Setup mysqldb
dbConnection = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{name}".format(
    user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST, port=DATABSE_PORT, name=DATABASE_NAME))

# Set up the app
app = Flask(__name__)

# Set up the controllers
pokemonController = PokemonController(dbConnection)

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
