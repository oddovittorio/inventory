import tkinter as tk
from tkinter import ttk
from crud_operations import view_products, add_product, delete_product 

# 1. Hauptfenster erstellen
root = tk.Tk()
root.title("Inventory Management")

# 2. Hauptcontainer in zwei Frames unterteilen
# Left-Frame für die Produktliste
left_frame = ttk.Frame(root, padding="10")
left_frame.grid(row=0, column=0, sticky="nsew")

# Right-Frame für CRUD-Buttons und Searchbar
right_frame = ttk.Frame(root, padding="10")
right_frame.grid(row=0, column=1, sticky="nsew")

# 3. Grid-Konfiguration, damit sich die Frames anpassen, wenn das Fenster skaliert wird
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# 4. Funktionen für die Datenbankoperationen
def update_listbox():
    # Leere zuerst die Listbox von Zeile null bis zum Ende
    product_listbox.delete(0, tk.END)
    
    # Rufe die view_products-Funktion auf, die eine Liste von Produkten zurückgibt
    products = view_products()
    
    # Falls Produkte vorhanden sind, füge sie der Listbox hinzu
    if products:
        for product in products:
            product_listbox.insert(tk.END, product) #Mit jedem Durchlauf der Schleife wird ein Produkt an das Ende der Listbox angehängt, sodass am Ende alle Produkte in der Reihenfolge ihrer Iteration angezeigt werden.
    else:
        product_listbox.insert(tk.END, "Keine Produkte gefunden!")

# Im Left-Frame: Produktliste

# Label für die Produktliste
list_label = ttk.Label(left_frame, text="Produktliste:")
list_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

# Listbox zur Anzeige der Produkte
product_listbox = tk.Listbox(left_frame, width=40, height=20)
product_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Scrollbar, die an die Listbox gebunden wird
scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=product_listbox.yview)
scrollbar.grid(row=1, column=1, sticky="ns", padx=5, pady=5)

# Die Listbox so konfigurieren, dass sie die Scrollbar nutzt
product_listbox.config(yscrollcommand=scrollbar.set)

# Refresh-Button zum Aktualisieren der Liste (zum Beispiel später verbunden mit view_products())
refresh_button = ttk.Button(left_frame, text="Aktualisieren", command=update_listbox)
refresh_button.grid(row=2, column=0, sticky="w", padx=5, pady=5)

# Mainloop starten
root.mainloop()