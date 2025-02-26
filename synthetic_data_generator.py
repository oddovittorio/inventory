# Mithilfe dieses Moduls können synthetische Daten generiert werden, die Sie am Ende in Ihre Datenbank einfügen können. Dieses Modul ist nützlich, wenn Sie eine Testumgebung für Ihre Anwendung erstellen möchten, ohne echte Daten zu verwenden. Es kann auch hilfreich sein, wenn Sie an einem Prototyp arbeiten und Beispieldaten benötigen, um die Funktionalität zu testen.

import random
import csv
from faker import Faker
import itertools

# Faker-Objekt mit deutscher Lokalisierung (wird hier z.B. für zufällige Farben verwendet)
fake = Faker('de_DE')

# Feste Definitionen für Klamotten

# Marken für Klamotten – nur diese verwenden
clothing_brands = ["Nike", "Adidas", "Puma", "Levi's"]

# Für jede Marke definieren wir Basisprodukte mit ca. 15 Einträgen (hier haben wir exemplarisch Listen)
clothing_products = {
    "Nike": [
        "Nike Sportswear Hoodie", "Nike Dri-FIT T-Shirt", "Nike Flex Pants",
        "Nike Air Zoom Running Shorts", "Nike Pro Leggings", "Nike Tech Fleece Joggers",
        "Nike Windrunner Jacket", "Nike Essentials Sweatshirt", "Nike Training Pants",
        "Nike VaporMax T-Shirt", "Nike Academy Sweatpants", "Nike Graphic Tee",
        "Nike Heritage Jacket", "Nike Performance Shorts", "Nike Mesh Hoodie"
    ],
    "Adidas": [
        "Adidas Originals Hoodie", "Adidas Originals T-Shirt", "Adidas Track Pants",
        "Adidas Originals Pullover", "Adidas Essentials Joggers", "Adidas Campus Sweatshirt",
        "Adidas Performance Shorts", "Adidas Superstar Fleece Jacket", "Adidas Primeblue Leggings",
        "Adidas Climalite Tee", "Adidas Sports Jacket", "Adidas Active Pants",
        "Adidas Essentials Hoodie", "Adidas Graphic T-Shirt", "Adidas Training Pants"
    ],
    "Puma": [
        "Puma Club Hoodie", "Puma Graphic T-Shirt", "Puma Essentials Jeans",
        "Puma Sporty Sweatpants", "Puma Active Hoodie", "Puma Runner Tee",
        "Puma Essentials T-Shirt", "Puma Track Jacket", "Puma Training Shorts",
        "Puma Flex Joggers", "Puma Classic Sweatshirt", "Puma Performance Pants",
        "Puma Modern Hoodie", "Puma Urban T-Shirt", "Puma Casual Jacket"
    ],
    "Levi's": [
        "Levi's 501 Original Jeans", "Levi's Denim Jacket", "Levi's Slim Fit Jeans",
        "Levi's 511 Skinny Jeans", "Levi's 505 Regular Fit Jeans", "Levi's Trucker Jacket",
        "Levi's Vintage T-Shirt", "Levi's Classic Pullover", "Levi's Bootcut Jeans",
        "Levi's 514 Straight Fit Jeans", "Levi's Relaxed Fit Pants", "Levi's 527 Slim Bootcut Jeans",
        "Levi's Denim Shirt", "Levi's 512 Slim Tapered Jeans", "Levi's Cargo Pants"
    ]
}

# Feste Größen für Klamotten
clothing_sizes = ["XXS", "XS", "S", "M", "L", "XL", "XXL"]

# Feste Farben für alle (optional: hier verwenden wir eine Liste, statt Faker für Farbe zu nutzen)
clothing_colors = ["Schwarz", "Weiß", "Blau", "Rot", "Grau"]

# Preisbereich für Klamotten
clothing_price_range = (10.0, 100.0)


# Feste Definitionen für Sneaker

# Marken für Sneaker (alle neun Marken)
sneaker_brands = ["Nike", "Adidas", "Puma", "Reebok", "New Balance", "Asics", "Under Armour", "Converse", "Vans"]

# Für jede Sneaker-Marke ca. 15 Modelle definieren
sneaker_products = {
    "Nike": [
        "Nike Dunk SB", "Nike Air Max 90", "Nike Air Force 1", "Nike React Element 87",
        "Nike Blazer Mid", "Nike Zoom Pegasus", "Nike Air VaporMax", "Nike Cortez",
        "Nike Free Run", "Nike Hyperdunk", "Nike Air Jordan 1", "Nike Air Zoom Pegasus 37",
        "Nike Air Huarache", "Nike SB Dunk Low", "Nike Shox"
    ],
    "Adidas": [
        "Adidas Superstar", "Adidas Ultraboost", "Adidas NMD_R1", "Adidas Stan Smith",
        "Adidas Samba", "Adidas Yeezy Boost 350", "Adidas Predator", "Adidas Copa Mundial",
        "Adidas Continental 80", "Adidas ZX Flux", "Adidas Forum Low", "Adidas Deerupt",
        "Adidas EQT Support", "Adidas Torsion X", "Adidas Crazy Explosive"
    ],
    "Puma": [
        "Puma RS-X", "Puma Cali", "Puma Future Rider", "Puma Suede Classic",
        "Puma Thunder Spectra", "Puma Basket", "Puma Flyer", "Puma Cell",
        "Puma Smash", "Puma King", "Puma Rider", "Puma Disc Blaze",
        "Puma UltraRide", "Puma Essential Rider", "Puma Legacy Rider"
    ],
    "Reebok": [
        "Reebok Classic", "Reebok Nano X", "Reebok ZigTech", "Reebok Instapump Fury",
        "Reebok Club C", "Reebok Workout Plus", "Reebok DMX Series", "Reebok Aztrek",
        "Reebok Legacy Lifter", "Reebok Floatride", "Reebok Rebel", "Reebok DMX Run 10",
        "Reebok CrossFit Nano", "Reebok Ventilator", "Reebok RX 100"
    ],
    "New Balance": [
        "New Balance 990", "New Balance 574", "New Balance 997", "New Balance 1080",
        "New Balance FuelCell", "New Balance Fresh Foam", "New Balance 880", "New Balance 997H",
        "New Balance 327", "New Balance 608", "New Balance 247", "New Balance Numeric",
        "New Balance 860", "New Balance 1500", "New Balance 520"
    ],
    "Asics": [
        "Asics Gel-Lyte III", "Asics Gel-Kayano 27", "Asics Gel-Nimbus", "Asics Gel-Quantum",
        "Asics GT-2000", "Asics Gel-Cumulus", "Asics Gel-Saga", "Asics Gel-DS Trainer",
        "Asics Gel-Resolution", "Asics Gel-Lyte V", "Asics Gel-Fujitrabuco", "Asics Gel-Lyte Runner",
        "Asics Gel-Venture", "Asics Gel-Kinsei", "Asics Gel-Noosa"
    ],
    "Under Armour": [
        "Under Armour Curry", "Under Armour HOVR Phantom", "Under Armour Charged Assert", "Under Armour Spawn",
        "Under Armour Micro G", "Under Armour TriBase", "Under Armour Scuba", "Under Armour Highlight MC",
        "Under Armour Project Rock", "Under Armour Speedform", "Under Armour HOVR Apex", "Under Armour HOVR Sonic",
        "Under Armour Ignite", "Under Armour Spawn 3", "Under Armour Flow"
    ],
    "Converse": [
        "Converse Chuck Taylor All-Star", "Converse One Star", "Converse Jack Purcell", "Converse Run Star Hike",
        "Converse Pro Leather", "Converse Fastbreak", "Converse CONS", "Converse CTAS",
        "Converse L6", "Converse All-Star Pro", "Converse Chuck Taylor 70", "Converse Platform",
        "Converse Hi-Top", "Converse Renew", "Converse Comfort"
    ],
    "Vans": [
        "Vans Old Skool", "Vans Era", "Vans Sk8-Hi", "Vans Authentic",
        "Vans Slip-On", "Vans Classic Slip-On", "Vans Checkerboard", "Vans Custom",
        "Vans Low Pro", "Vans UltraRange", "Vans Old Skool Pro", "Vans Sk8-Hi Pro",
        "Vans Modern", "Vans Field", "Vans Vault"
    ]
}

# Feste Schuhgrößen (als Strings) für Sneaker: 37 bis 46
sneaker_sizes = [str(x) for x in range(37, 47)]

# Feste Farben für Sneaker (können dieselben sein wie für Kleidung oder angepasst werden)
sneaker_colors = ["Schwarz", "Weiß", "Grau", "Rot", "Blau"]

# Preisbereich für Sneaker
sneaker_price_range = (50.0, 200.0)

# Preisbereich für Klamotten bleibt wie gehabt
# clothing_price_range = (10.0, 100.0)

def generate_fixed_product_catalog():
    """
    Generiert einen festen Produktkatalog, bei dem für jede Kombination aus Marke,
    Basisprodukt, Größe und Farbe ein eigener Eintrag (mit eindeutiger Artikelnummer) erzeugt wird.
    Gibt eine Liste von Tupeln zurück: (artikelnummer, beschreibung, farbe, größe, kategorie, marke, preis)
    """
    variants = []
    artikelnummer = 1000  # Startwert für Artikelnummern

    # Für Klamotten
    for brand in clothing_brands:
        for product in clothing_products[brand]:
            for size, color in itertools.product(clothing_sizes, clothing_colors):
                # Hier kann der Preis entweder fix oder zufällig innerhalb eines Bereichs sein
                preis = round(random.uniform(clothing_price_range[0], clothing_price_range[1]), 2)
                variants.append((artikelnummer, product, color, size, "Klamotten", brand, preis))
                artikelnummer += 1

    # Für Sneaker
    for brand in sneaker_brands:
        for product in sneaker_products[brand]:
            for size, color in itertools.product(sneaker_sizes, sneaker_colors):
                preis = round(random.uniform(sneaker_price_range[0], sneaker_price_range[1]), 2)
                variants.append((artikelnummer, product, color, size, "Sneaker", brand, preis))
                artikelnummer += 1

    return variants

# Anzahl der zu generierenden Datensätze wird nun durch den festen Katalog bestimmt
catalog = generate_fixed_product_catalog()

# Schreibe den Katalog in eine CSV-Datei
with open('product_catalog.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["artikelnummer", "beschreibung", "farbe", "größe", "kategorie", "marke", "preis"])
    for record in catalog:
        writer.writerow(record)

print(f"{len(catalog)} Produktvarianten wurden in product_catalog.csv geschrieben.")