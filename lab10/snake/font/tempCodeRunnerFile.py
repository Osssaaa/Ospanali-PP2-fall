import psycopg2
from config import load_config  
config = load_config()
command = """DROP TABLE usernames;"""
try:
    with psycopg2.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(command)
except (psycopg2.DatabaseError, Exception) as error:
        print(error)