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

    cursor.execute("INSERT INTO Teachers VALUES("
                   "1, "
                   "'James Smith', "
                   "'jsmith@wcpss.net', "
                   "'1234567')")
    cursor.execute("INSERT INTO Teachers VALUES("
                   "2, "
                   "'Jane Smith', "
                   "'smith2@wcpss.net', "
                   "'7654321')")
    cursor.execute("INSERT INTO Students VALUES("
                   "1, "
                   "'Adam Longlegs', "
                   "'alonglegs@students.wcpss.net', "
                   "'11235813')")
    cursor.execute("INSERT INTO Students VALUES("
                   "2, "
                   "'Mary Taylor', "
                   "'mtaylor@students.wcpss.net', "
                   "'12481632')")

    connection.commit()
    print("Values inserted successfully.")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
