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
            
def view_products():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM Produkte"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Keine Produkte gefunden!")
        except Error as e:
            print("Fehler beim Abrufen der Produkte:", e)
        finally:
            conn.close()  

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

def edit_product(product_id, updated_data):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """
            UPDATE Produkte
            SET beschreibung = %s, farbe = %s, größe = %s, kategorie = %s, marke = %s, preis = %s
            WHERE artikelnummer = %s
            """
            # Wir kombinieren updated_data und product_id, damit der letzte Platzhalter befüllt wird.
            cursor.execute(sql, updated_data + (product_id,))
            conn.commit()
            print("Produkt erfolgreich aktualisiert!")
        except Error as e:
            print("Fehler beim Aktualisieren des Produkts:", e)
        finally:
            conn.close()
