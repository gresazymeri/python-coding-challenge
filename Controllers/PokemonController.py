import pandas as panda
import os
from flask import request

class PokemonController:
    # Constructor
    def __init__(self, dbConnection):
        self.dbConnection = dbConnection

    # Get all pokemons
    def getAllFromDatabase(self):
        result = {}

        return result

    # Get all pokemons from csv
    def getAllFromCsv(self):
        # Declare needed variables
        filePath = os.path.abspath('Data/pokemon.csv')

        # Read csv file
        dataFrame = panda.read_csv(filePath)

        # Remove "#" column
        dataFrame = dataFrame.iloc[: , 1:]

        # Replace NAN with null
        dataFrame = dataFrame.where(panda.notnull(dataFrame), None)

        # Sorts
        if(request.args.get('sortByDesc')):
            columnsToSort = request.args.get('sortByDesc').split(',')
            dataFrame = dataFrame.sort_values(by=columnsToSort, ascending=False)

        if(request.args.get('sortByAsc')):
            columnsToSort = request.args.get('sortByAsc').split(',')
            dataFrame = dataFrame.sort_values(by=columnsToSort, ascending=True)

        # Filters
        if(request.args.get('filter[Type 1]')):
            dataFrame = dataFrame.loc[dataFrame['Type 1'] == request.args.get('filter[Type 1]')]
        if(request.args.get('filter[Type 2]')):
            dataFrame = dataFrame.loc[dataFrame['Type 2'] == request.args.get('filter[Type 2]')]

        # Convert the DataFrame to a dictionary
        dataFrame = dataFrame.to_dict(orient='records')

        # Return final response
        return  dataFrame

    # Import pokemons from file
    def importAllToDatabase(self):
        # Declare needed variables
        filePath = os.path.abspath('Data/pokemon.csv')

        # Read csv file
        dataFrame = panda.read_csv(filePath)

        # Remove "#" column
        dataFrame = dataFrame.iloc[: , 1:]

        # Insert to database
        dataFrame.to_sql(con=self.dbConnection, name='pokemons', if_exists='replace',index_label='id')

        # Return final response
        return {'success': 'true', 'message': 'Process was completed successfully!'}
