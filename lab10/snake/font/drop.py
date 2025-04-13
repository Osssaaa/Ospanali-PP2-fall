import psycopg2
from config import load_config

def drop_table():
    config = load_config()
    command = """DROP TABLE usernames;"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
if __name__ == "__main__":
    drop_table()