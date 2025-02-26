# Mithilfe dieses Moduls können synthetische Daten generiert werden, die Sie am Ende in Ihre Datenbank einfügen können. Dieses Modul ist nützlich, wenn Sie eine Testumgebung für Ihre Anwendung erstellen möchten, ohne echte Daten zu verwenden. Es kann auch hilfreich sein, wenn Sie an einem Prototyp arbeiten und Beispieldaten benötigen, um die Funktionalität zu testen.

import random
import csv
from faker import Faker

# Faker-Objekt mit deutscher Lokalisierung
fake = Faker('de_DE')

def generate_fake_product():
    """
    Generiert ein Fake-Produkt als Tuple, passend zu unserem Schema:
    (artikelnummer, beschreibung, farbe, größe, kategorie, marke, preis)
    """
    # Artikelnummer: Zufallszahl zwischen 1000 und 9999
    artikelnummer = random.randint(1000, 9999)
    
    # Kategorie zufällig wählen
    kategorie = random.choice(["Klamotten", "Sneaker"])
    
    if kategorie == "Klamotten":
        # Für Klamotten: Wähle einen Produkttyp
        produkt_typ = random.choice(["Hoodie", "Hose", "Jacke", "T-Shirt", "Pullover", "Jeans"])
        beschreibung = produkt_typ  # Beschreibung entspricht hier dem Produkttyp
        
        # Größen für Klamotten
        größen = ["XXS", "XS", "S", "M", "L", "XL", "XXL"]
        größe = random.choice(größen)
        
        # Preisbereich für Klamotten: z. B. 10,00 bis 100,00 €
        preis = round(random.uniform(10.0, 100.0), 2)
        
        # Auswahl echter Marken für Klamotten (oder allgemeine Marken)
        marken_liste = ["Nike", "Adidas", "Puma", "Levi's", "H&M", "Zara", "Uniqlo"]
        marke = random.choice(marken_liste)
    else:
        # Für Sneaker: Wähle einen Produkttyp, der zu Schuhen passt
        produkt_typ = random.choice(["Sneaker", "Laufschuhe", "Sportschuhe"])
        beschreibung = produkt_typ  # Beschreibung ist der gewählte Produkttyp
        
        # Schuhgrößen von 37 bis 46
        größen = list(range(37, 47))
        größe = str(random.choice(größen))  # Als String speichern
        
        # Preisbereich für Sneaker: z. B. 50,00 bis 200,00 €
        preis = round(random.uniform(50.0, 200.0), 2)
        
        # Auswahl von echten Sneaker-Marken
        marken_liste = ["Nike", "Adidas", "Puma", "Reebok", "New Balance", "Asics", "Under Armour", "Converse", "Vans"]
        marke = random.choice(marken_liste)
    
    # Farbe: Zufällig generiert
    farbe = fake.color_name()
    
    return (artikelnummer, beschreibung, farbe, größe, kategorie, marke, preis)

# Anzahl der zu generierenden Datensätze
NUM_RECORDS = 10000

# Erstelle die CSV-Datei und schreibe die Daten hinein
with open('fake_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Schreibe die Kopfzeile
    writer.writerow(["artikelnummer", "beschreibung", "farbe", "größe", "kategorie", "marke", "preis"])
    
    # Generiere und schreibe die Datensätze
    for _ in range(NUM_RECORDS):
        writer.writerow(generate_fake_product())

print(f"{NUM_RECORDS} Datensätze wurden in fake_products.csv geschrieben.")