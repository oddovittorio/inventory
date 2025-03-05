from db_connection import create_connection
from mysql.connector import Error

def view_products_with_stock(search_query=None):
    """
    Führt einen JOIN zwischen den Tabellen 'Produkte' und 'Bestand' durch,
    um alle Produktinformationen zusammen mit dem Lagerbestand zurückzugeben.
    Optional: Filtert die Ergebnisse anhand des Suchbegriffs über alle Attribute.
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
            params = []
            # Wenn ein Suchbegriff vorliegt, erweitere die Abfrage um alle relevanten Spalten
            if search_query:
                sql += """
                WHERE 
                    CAST(p.Artikelnummer AS CHAR) LIKE %s OR
                    p.Kategorie LIKE %s OR
                    p.Marke LIKE %s OR
                    p.Beschreibung LIKE %s OR
                    p.Größe LIKE %s OR
                    CAST(p.Preis AS CHAR) LIKE %s OR
                    p.Farbe LIKE %s OR
                    CAST(b.bestandsanzahl AS CHAR) LIKE %s
                """
                search_term = "%" + search_query + "%"
                params = [search_term] * 8  # 8 mal den gleichen Suchbegriff
            cursor.execute(sql, params)
            products = cursor.fetchall()
        except Error as e:
            print("Fehler beim Abrufen der Produkte mit Bestand:", e)
        finally:
            conn.close()
    return products