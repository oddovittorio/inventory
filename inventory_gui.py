import tkinter as tk
from tkinter import ttk
from crud_operations import view_products, add_product, delete_product
from inventory_queries import view_products_with_stock

root = tk.Tk()
root.title("Inventory Management")

# Frames
left_frame = ttk.Frame(root, padding="10")
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = ttk.Frame(root, padding="10")
right_frame.grid(row=0, column=1, sticky="nsew")

# Grid-Konfiguration
root.columnconfigure(0, weight=1) # Parameter: index (=Also welche Spalte angesprochen wird), weight (=Wie viel Platz die Spalte einnehmen soll beim Vergrößern des Fensters)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

left_frame.rowconfigure(1, weight=1)
left_frame.columnconfigure(0, weight=1)

# ____________________Left Frame____________________  #

# Label für die Produktliste
list_label = ttk.Label(left_frame, text="Produktliste:")
list_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

# ----- TREEVIEW -----
columns = ("artikelnummer", "kategorie", "marke", "beschreibung", "groesse", "preis", "farbe", "bestand")
product_tree = ttk.Treeview(left_frame, columns=columns, show="headings")
product_tree.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Spaltenüberschriften
product_tree.heading("artikelnummer", text="Artikelnummer")
product_tree.heading("kategorie", text="Kategorie")
product_tree.heading("marke", text="Marke")
product_tree.heading("beschreibung", text="Beschreibung")
product_tree.heading("groesse", text="Größe")
product_tree.heading("preis", text="Preis")
product_tree.heading("farbe", text="Farbe")
product_tree.heading("bestand", text="Bestand")

# Optionale Spaltenbreiten
product_tree.column("artikelnummer", width=100)
product_tree.column("beschreibung", width=200)
product_tree.column("farbe", width=50) 
product_tree.column("groesse", width=50)
product_tree.column("kategorie", width=100)
product_tree.column("marke", width=100)
product_tree.column("preis", width=50)
product_tree.column("bestand", width=50)

# Scrollbar für das Treeview
scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=product_tree.yview)
scrollbar.grid(row=1, column=1, sticky="ns", padx=5, pady=5)
product_tree.configure(yscrollcommand=scrollbar.set)

# Update-Funktion
def update_treeview():
    product_tree.delete(*product_tree.get_children())
    products = view_products_with_stock()
    if products:
        for product in products:
            # product = (artikelnummer, beschreibung, farbe, größe, kategorie, marke, preis)
            product_tree.insert("", tk.END, values=product)
    else:
        pass

# Refresh-Button
refresh_button = ttk.Button(left_frame, text="Aktualisieren", command=update_treeview)
refresh_button.grid(row=2, column=0, sticky="w", padx=5, pady=5)

# ----- Treeview ENDE -----

# ____________________Right Frame____________________  #

# Search-Label
search_label = ttk.Label(right_frame, text="Suche:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

search_entry = ttk.Entry(right_frame, width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

search_button = ttk.Button(right_frame, text="Suchen", command=lambda: search_products())
search_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

root.mainloop()