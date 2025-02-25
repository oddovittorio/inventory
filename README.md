# inventory

## MySQL-Database
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
