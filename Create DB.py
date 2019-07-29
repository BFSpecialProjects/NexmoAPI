# requires postgreSQL
# pip install psycopg2
import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(host="localhost",
                                  database="Nestwatch",
                                  port="5432",
                                  user="postgres",
                                  password="azedsuop")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.execute("""
    CREATE TABLE Teachers(
    ID_Number integer PRIMARY KEY,
    Name text,
    Email text,
    Phone_Number text)
    """)
    print("Table Teachers created successfully")

    cursor.execute("""
   CREATE TABLE Students(
    ID_Number integer PRIMARY KEY,
    Name text,
    Email text,
    Phone_Number text)
    """)
    connection.commit()
    print("Table Students created successfully")

    cursor.execute("""
    CREATE TABLE Messages(
     ID_Number integer PRIMARY KEY,
     Threat text,
     Location text,
     Notes text)
     """)
    connection.commit()
    print("Table Messages created successfully")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
