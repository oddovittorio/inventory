from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def create_connection():
  try:
    connection = mysql.connector.connect(
      host=DB_HOST,
      user=DB_USER,
      password=DB_PASSWORD,
      database=DB_NAME
    )
    if connection.is_connected():
      print("Connected to the database")
      return connection
  except Error as e:
    print("Error while connecting to the database: {e}")
    return None
  
  ## Debugging:
  
  if __name__ == "__main__":
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Testabfrage erfolgreich, Ergebnis:", result)
        except Error as e:
            print("Fehler bei der Testabfrage:", e)
        finally:
            conn.close()