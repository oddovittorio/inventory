from db_connection import create_connection
from mysql.connector import Error

def view_products_with_stock():
    """
    Führt einen JOIN zwischen den Tabellen 'Produkte' und 'Bestand' durch,
    um alle Produktinformationen zusammen mit dem Lagerbestand zurückzugeben.
    """
    conn = create_connection()
    products = []
    if conn:
        try:
            cursor = conn.cursor()
            sql = """
            SELECT p.Artikelnummer, p.Kategorie, p.Marke, p.Beschreibung, p.Größe, p.Preis, p.Farbe, b.bestandsanzahl
            FROM Produkte p
            JOIN Bestand b ON p.Artikelnummer = b.Artikelnummer
            """
            cursor.execute(sql)
            products = cursor.fetchall()
        except Error as e:
            print("Fehler beim Abrufen der Produkte mit Bestand:", e)
        finally:
            conn.close()
    return products