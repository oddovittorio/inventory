from db_connection import create_connection
from mysql.connector import Error

# CRUD operations

def add_product(product):
  conn = create_connection()
  if conn:
        try:
            cursor = conn.cursor()
            sql = """
            INSERT INTO Produkte(Artikelnummer, Beschreibung, Farbe, Größe, Kategorie, Marke, Preis)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, product)
            conn.commit()
            print("Produkt erfolgreich hinzugefügt!")
        except Error as e:
            print("Fehler beim Hinzufügen des Produkts:", e)
        finally:
            conn.close()
  
#def view_products():
  
#def edit_product(product_id, updated_data)

#def delete_product(product_id):
