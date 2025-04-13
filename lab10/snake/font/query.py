import psycopg2
from config import load_config


def query(name):
    sql = 'SELECT * FROM usernames WHERE Name = %s'

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name,))
                rows = cursor.fetchall()
                for row in rows:    
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при запросе:", error)

if __name__ == '__main__':
    x = query("Kanagat")
   