# inventory

## MySQL-Database
### Lagerart:
Das System bildet ein Lager für einen Einzelhandel ab, 

### Benötigte Tabellen:
**Produkttabelle:** Enthält alle im EInzelhandel geführten Produkte.
**Lagerbestandstabelle:** Erfasst den aktuellen Bestand der Produkte.

### Tabellen:
***Produkte***(Artikelnummer, Kategorie, Marke, Beschreibung, Größe, Preis, Farbe)
Primary Key -> {Artikelnummer}

***Bestand***(Artikelnummer, Bestandsanzahl)

### Fazit:
Das vorgestellte Datenmodell bildet die Grundlage für ein einfaches, aber erweiterbares Lagerverwaltungssystem. Es gewährleistet die Datenintegrität zwischen den Tabellen und ermöglicht in späteren Erweiterungen die Einbindung von Verkaufsdaten, Kundenbestellungen oder zusätzlichen Lagerinformationen.
