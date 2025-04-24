import pdfplumber as pdf

# Hier werden die einzelnen Daten eingelesen und entsprechend analysiert
# Definition der Dateipfade
dateipfad_muenchen = "ergebnislisten/ergebnisliste_muenchen.pdf"
dateipfad_koeln = "ergebnislisten/ergebnisliste_koeln.pdf"
dateipfad_freiburg = "ergebnislisten/ergebnisliste_freiburg.pdf"
dateipfad_zuerich = "ergebnislisten/ergebnisliste_zuerich.pdf"

def einlesen_muenchen():
    inhalt = ""
    try:
        with pdf.open(dateipfad_muenchen) as file:
           for page in file.pages:
                inhalt += page.extract_text()
    except:
        print(f"Der Dateipfad {dateipfad_muenchen} ist nicht bekannt.\n Bitte diesen dementsprechend abaendern")
    return inhalt

def einlesen_koeln():
    inhalt = ""
    try:
        with pdf.open(dateipfad_koeln) as file:
            for page in file.pages:
                inhalt += page.extract_text()
    except:
        print(f"Der Dateipfad {dateipfad_koeln} ist nicht bekannt.\n Bitte diesen dementsprechend abaendern")
    return inhalt

def einlesen_freiburg():
    inhalt = ""
    try:
        with pdf.open(dateipfad_freiburg) as file:
            for page in file.pages:
                inhalt += page.extract_text()
    except:
        print(f"Der Dateipfad {dateipfad_freiburg} ist nicht bekannt.\n Bitte diesen dementsprechend abaendern")
    return inhalt

def einlesen_zuerich():
    inhalt = ""
    try:
        with pdf.open(dateipfad_zuerich) as file:
            for page in file.pages:
                inhalt += page.extract_text()
    except:
        print(f"Der Dateipfad {dateipfad_zuerich} ist nicht bekannt.\n Bitte diesen dementsprechend abaendern")
    return inhalt

def daten_analyse_muenchen(daten):
    dictionary_muenchen = {}
    schluessel = ""
    schluessel_int = 0
    nation = ""
    jahrgang = ""
    geschlecht = ""
    zielzeit = ""
    daten = daten.split("\n")                       # Daten nach Zeilen sortieren
    for zeile in daten:                             # Auslesen der Daten
        daten_liste = []
        if zeile.strip():                       
            zeile = zeile.split()
            schluessel = zeile[0]                   # Platzierung als Schlüssel
            schluessel = schluessel.replace(".", "")
            try:
                schluessel_int = int(schluessel)
            except:
                continue
            for element in zeile:                   # Restliche Daten ermitteln
                if len(element) == 4 and element.isdigit():
                    jahrgang = element
                elif len(element) == 3 and element.isalpha() and element.isupper():
                    nation = element
                elif element.count(":") == 2 and element.count("(") == 0:
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha and element.isupper()) or (len(element) == 3 and element[0].isalpha() and element[1].isdigit() and element[2].isdigit()):                   
                    if len(element) == 3:           # Filtert das Geschlecht, je nach mit oder ohne Angabe der Altersklasse
                        geschlecht = element[0]
                    else:
                        geschlecht = element
            daten_liste.append(zielzeit)            # Daten in ein Dictionary zur Weiterverarbeitung speichern
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append(nation)
            dictionary_muenchen[schluessel_int] = daten_liste
    return dictionary_muenchen

def daten_analyse_freiburg(daten):
    dictionary_freiburg = {}
    schluessel = ""
    schluessel_int = 0
    nation = ""
    jahrgang = ""
    geschlecht = ""
    zielzeit = ""
    daten = daten.split("\n")                       # Daten nach Zeilen sortieren
    for zeile in daten:                             # Auslesen der Daten
        daten_liste = []
        if zeile.strip():                       
            zeile = zeile.split()
            schluessel = zeile[0]                   # Platzierung als Schlüssel
            schluessel = schluessel.replace(".", "")
            try:
                schluessel_int = int(schluessel)
            except:
                continue
            for element in zeile:                   # Restliche Daten ermitteln
                if len(element) == 4 and element.isdigit():
                    jahrgang = element
                elif element.count(":") == 2:
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha and element.islower()):                   
                        geschlecht = element
            daten_liste.append(zielzeit)            # Daten in ein Dictionary zur Weiterverarbeitung speichern
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append("u")                 # Nationen als undefined setzen
            dictionary_freiburg[schluessel_int] = daten_liste
    return dictionary_freiburg

def daten_analyse_zuerich(daten):
    dictionary_zuerich = {}
    schluessel = ""
    schluessel_int = 0
    nation = ""
    jahrgang = ""
    geschlecht = ""
    zielzeit = ""
    count = 0
    daten = daten.split("\n")                       # Daten nach Zeilen sortieren
    for zeile in daten:                             # Auslesen der Daten
        daten_liste = []
        if zeile.strip():                       
            zeile = zeile.split()
            schluessel = zeile[0]                   # Platzierung als Schlüssel
            schluessel = schluessel.replace(".", "")
            try:
                schluessel_int = int(schluessel)
            except:
                continue
            for element in zeile:                   # Restliche Daten ermitteln
                if len(element) == 4 and element.isdigit() and count != 1:
                    jahrgang = element
                elif len(element) == 3 and element.isalpha() and element.isupper():
                    nation = element
                elif element.count(":") == 2:
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha and element.isupper()):                   
                    geschlecht = element
                count += 1                          # Hilsvariable zum Bestimmmen des Jahrgangs
            daten_liste.append(zielzeit)            # Daten in ein Dictionary zur Weiterverarbeitung speichern
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append(nation)
            dictionary_zuerich[schluessel_int] = daten_liste
            count = 0                               # Zurücksetzen der Hilfsvariable
    return dictionary_zuerich

def main_daten_select():
    daten_muenchen = einlesen_muenchen()
    dictionary_muenchen = daten_analyse_muenchen(daten_muenchen)
    daten_freiburg = einlesen_freiburg()
    dictionary_freiburg = daten_analyse_freiburg(daten_freiburg)
    daten_zuerich = einlesen_zuerich()
    dictionary_zuerich = daten_analyse_zuerich(daten_zuerich)

main_daten_select()
