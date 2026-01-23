import os
import pymysql
from dotenv import load_dotenv

load_dotenv()


class Repository:    # metodo per ottenimento connessione al db

    def get_connection(self):
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "amazon_sales")
        )

    # metodo generico standard di manipolazione dati
    def manipolazione_dati(self,sql,valori):
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,valori)
                    connection.commit()
                    cursor.rowcount
        except Exception as e:
            print(e)
            return "errore database"
        

    # metodo generico standard per recupero dati multipli 

    def recupero_multiplo(self,sql,valori=None):
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    if valori:
                        cursor.execute(sql,valori)
                    else:
                        cursor.execute(sql)
                    return cursor.fetchall()
        except Exception as e:
            print(e)
            return "errore database"
        


        # metodo generico standard per recupero dato singolo 

    def recupero_singolo(self,sql,valori):
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,valori)
                    return cursor.fetchone()
        except Exception as e:
            print(e)
            return "errore database"
