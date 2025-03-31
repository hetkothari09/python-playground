import psycopg2
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:root@localhost:5432/demo-db'
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# cursor.execute("SELECT version();")
# cursor.execute("SELECT * FROM employee;")
# print(cursor.fetchone())


# We use SQLAlchemy to write queries instead of using psycopg2 because:
# 1. SQLAlchemy sits on top of psycopg2 and provides abstraction
# 2. Psycopg2 creates a new connection request for each query which is time-consuming and not efficient
# 3. SQLAlchemy on the other hand handles connection pool, which reuses connections
# 4. Writing queries with SQLAlchemy is better as parameter passing etc., is good.


db_string = DATABASE_URL
engine = create_engine(DATABASE_URL)


data_to_insert = [
    {"name": "Porche", "model": "911", "year": 2004},
    {"name": "BMW", "model": "M3", "year": 2011},
    {"name": "Lamborghini", "model": "Urus", "year": 2015},
]


with engine.connect() as connection:
    # results = connection.execute(text("SELECT * FROM employee"))
    # for i in results:
    #     print(i)

    # connection.execute(text(
    #     """
    #     CREATE TABLE IF NOT EXISTS cars (id SERIAL PRIMARY KEY, name VARCHAR(255), model VARCHAR(255), year INT);
    #     """
    # ))

    # connection.execute(text(
    #     """ INSERT INTO cars(name, model, year) VALUES (:name, :model, :year)"""),
    #     data_to_insert
    # )

    # results = connection.execute(text(
    #     """
    #     SELECT * FROM cars;
    #     """
    # ))
    #
    # for i in results:
    #     print(i)


    # connection.execute(text(
    #     """
    #     UPDATE cars
    #     SET model = 'M2'
    #     WHERE name = 'BMW';
    #     """
    # ))

    results2 = connection.execute(text(
        """
        SELECT * FROM cars
        ORDER BY id;
        """
    ))

    for i in results2:
        print(i)


    # connection.commit is necessary whenever you run any CRUD operations
    # connection.commit()

