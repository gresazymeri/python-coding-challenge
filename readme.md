# Introduction

This project is a python coding challange.

### Requirements

Expose the data from `pokemon.csv` file, through an API endpoint. Feel free to use any of the python frameworks: DjangoRESTFramework, FastAPI, Flask, etc. Use a DBMS (PostgreSQL, MySQL) for storing the data.

A Client of the API should be able to:
- Sort by at least two columns in ascending or descending order.
- Flter by pokemon type

### Installation

To install the project, you need to install those packages:

```bash
pip3 install flask pymysql python-dotenv pandas sqlalchemy flask_sqlalchemy
```

### Start app

Go to the project dir and create `.env` file, you need to copy the content of `.env.example` file.

Open `.env` file and start configuring the database.

Now you are ready to start your app with this script below:

```bash
python3 app.py
```

This starts a local server, which will watch for any file changes and will restart the server according to these changes. The server address will be displayed to you as http://127.0.0.1:5000.

### API

To test available endpoints, you can use Postman (or Insomnia) or any other REST client.

Below you can see the available endpoints:

---

URL: http://127.0.0.1:5000/database/pokemons/import

Description: Import the data from `pokemon.csv` file to database.

---

---

URL: http://127.0.0.1:5000/csv/pokemons

Description: Get all pokemons from the csv.

Available query parameters:

`sortByDesc` (To sort multiple columns in descending order, all columns all available for sorting).
Example: `http://127.0.0.1:5000/csv/pokemons?sortByDesc=HP,Defense`.

`sortByAsc` (To sort multiple columns in ascending order, all columns all available for sorting).
Example: `http://127.0.0.1:5000/csv/pokemons?sortByAsc=HP,Defense`.

`filter` (To filter Type 1 or Type 2 column, only Type 1 and Type 2 all available for filtering).
Example: `http://127.0.0.1:5000/csv/pokemons?filter[Type 1]=Bug`.

---

---

URL: http://127.0.0.1:5000/database/pokemons

Description: Get all pokemons from the database.

Available query parameters:

`sortByDesc` (To sort specifc column in descending order).
Example: `http://127.0.0.1:5000/csv/pokemons?sortByDesc=HP`.

`sortByAsc` (To sort specifc column in ascending order).
Example: `http://127.0.0.1:5000/csv/pokemons?sortByAsc=HP,Defense`.

`filter` (To filter Type 1 or Type 2 column, only Type 1 and Type 2 all available for filtering).
Example: `http://127.0.0.1:5000/csv/pokemons?filter[Type 1]=Bug`.

---