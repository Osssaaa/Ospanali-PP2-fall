import psycopg2
from config import load_config

def create_table():
    config = load_config()
    command = """CREATE TABLE usernames (
                    Name varchar(255) PRIMARY KEY,
                    Level int,
                    Score int,
                    Length int,
                    FPS int
                );;"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
if __name__ == "__main__":
    create_table()