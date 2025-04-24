import pdfplumber as pdf

# Hier werden die einzelnen Daten eingelesen und entsprechend analysiert
# Definition der Dateipfade
dateipfad_muenchen = "ergebnislisten/ergebnisliste_muenchen.pdf"
dateipfad_koeln = "ergebnislisten/ergebnisliste_koeln.pdf"
dateipfad_freiburg = "ergebnislisten/ergenisliste_freiburg.pdf"
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
            nation = zeile[3]                       # Restliche Daten ermitteln
            jahrgang = zeile[5]
            geschlecht = zeile[6]
            zielzeit = zeile[9]
            daten_liste.append(zielzeit)
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append(nation)
            dictionary_muenchen[schluessel_int] = daten_liste
    return dictionary_muenchen

def main_daten_select():
    daten = einlesen_muenchen()
    dictionary = daten_analyse_muenchen(daten)
    print(dictionary)

main_daten_select()
