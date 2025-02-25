# inventory

## MySQL-Database implementieren
### Lagerart:
Das System bildet ein Lager für einen Einzelhandel ab, der verschiedene Produktkategorien (Klamotten und Sneaker) führt.

### Benötigte Tabellen:
**Produkttabelle:** Enthält alle im EInzelhandel geführten Produkte. <br>
**Lagerbestandstabelle:** Erfasst den aktuellen Bestand der Produkte.

### Tabellen:
***Produkte***(Artikelnummer, Kategorie, Marke, Beschreibung, Größe, Preis, Farbe) <br>
Primary Key -> {Artikelnummer} <br>

***Bestand***(Artikelnummer, Bestandsanzahl) <br>
Foreign Key -> {Artikelnummer} verweist auf ***Produkte***

### Fazit:
Das vorgestellte Datenmodell bildet die Grundlage für ein einfaches, aber erweiterbares Lagerverwaltungssystem.<br>Es gewährleistet die Datenintegrität zwischen den Tabellen und ermöglicht in späteren Erweiterungen die Einbindung von Verkaufsdaten, Kundenbestellungen oder zusätzlichen Lagerinformationen.

### CRUD-Operationen implementieren
Um die Verwaltung der Produktdaten in der Datenbank zu ermöglichen, werden grundlegende CRUD-Funktionen (Create, Read, Update, Delete) entwickelt. <br> Diese Funktionen bilden das Rückgrat des Backends und dienen als Basis für spätere Erweiterungen und die Integration in eine grafische Benutzeroberfläche.

## Funktionen:
 - ***add_product()*** <br>
*Funktion:* Fügt ein neues Produkt in die Produkttabelle ein. <br>
*Aufgaben:* Validierung der Eingabedaten + Einfügen der Daten in die Datenbank <br>
- ***edit_product()*** <br>
*Funktion:* Bearbeitet die Informationen eines bestehenden Produkts. <br>
*Aufgaben:* Überprüfen ob Produkt existiert + Aktualisieren der Datenbank <br>
- ***delete_product()*** <br>
*Funktion:* Entfernt ein Produkt aus der Produkttabelle <br>
*Aufgaben:* Bestätigung der Löschung + Löschen des Eintrags in der Datenbank<br>
- ***view_products()*** <br>
*Funktion:* Ruft alle Produkte (oder eine gefilterte Auswahl) aus der Datenbank ab und zeigt sie an. <br>
*Aufgaben:* Abrufen der Produktliste aus der Datenbank + Rückgabe der Daten als Liste<br>

### Backend-Implementierung:
Die CRUD-Funktionen werden in Python realisiert und über direkte Datenbankverbindungen mit MySQL-Connector getestet.
