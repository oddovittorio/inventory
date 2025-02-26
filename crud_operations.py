from db_connection import create_connection
from mysql.connector import Error

# CRUD operations

def add_product(produkt):
  conn = create_connection()
  if conn:
        try:
            cursor = conn.cursor()
            sql = """
            INSERT INTO Produkte(Artikelnummer, Beschreibung, Farbe, Größe, Kategorie, Marke, Preis)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, produkt)
            conn.commit()
            print("Produkt erfolgreich hinzugefügt!")
        except Error as e:
            print("Fehler beim Hinzufügen des Produkts:", e)
        finally:
            conn.close()
  
#def view_products():
  
#def edit_product(artikelnummer, updated_data)

def delete_product(artikelnummer):
    """
    Löscht ein Produkt aus der Datenbank.
    
    Parameter:
        product_id (int): Die Artikelnummer des Produkts, das gelöscht werden soll.
    """
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # SQL-Statement, das das Produkt anhand der Artikelnummer löscht
            sql = "DELETE FROM Produkte WHERE Artikelnummer = %s"
            cursor.execute(sql, (artikelnummer,))
            conn.commit()
            print("Produkt erfolgreich gelöscht!")
        except Error as e:
            print("Fehler beim Löschen des Produkts:", e)
        finally:
            conn.close()
