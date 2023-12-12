from sqlalchemy import create_engine, text
import psycopg2
import os

class ApartmentsRepository:

    def __init__(self):
        self.__db_user = os.environ['DB_USER']
        self.__db_password = os.environ['DB_PASSWORD']
        self.__db_name = os.environ['DB_NAME']
        self.__db_host = os.environ['DB_HOST']
        self.__db_port = os.environ['DB_PORT']
        self.__db_string = f'postgresql://{self.__db_user}:{self.__db_password}@{self.__db_host}:{self.__db_port}/{self.__db_name}'
        #self.__db_string = 'postgresql://postgres:postgres@db:5432/apartmentsDB'
        self.__db = create_engine(self.__db_string)

    def create_apartments_table(self):
        with self.__db.connect() as conn:
            query = text("CREATE TABLE IF NOT EXISTS apartments (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, images TEXT[] NOT NULL);")
            conn.execute(query)
            conn.commit()
    def add_new_apartment(self,title, images):
        with self.__db.connect() as conn:
            query = text("INSERT INTO apartments (title, images) VALUES (:title, :images)")
            conn.execute(query, {'title':title, 'images':images})
            conn.commit()

    def get_all_apartments(self):
        with self.__db.connect() as conn:
            query = text("SELECT * FROM apartments")
            result = conn.execute(query)
            return result.fetchall()

    def count_apartments(self):
        with self.__db.connect() as conn:
            query = text("SELECT COUNT(*) FROM apartments")
            result = conn.execute(query)
            count = result.fetchone()[0]
            return count
