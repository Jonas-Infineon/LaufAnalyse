import pdfplumber as pdf
import threading as thread
import time as time
import logging

# Nur echte Fehler anstelle von Warnungen anzeigen
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Hier werden die einzelnen Daten eingelesen und entsprechend analysiert
# Definition der Dateipfade
dateipfad_muenchen = "ergebnislisten/ergebnisliste_muenchen.pdf"
dateipfad_freiburg = "ergebnislisten/ergebnisliste_freiburg.pdf"
dateipfad_zuerich = "ergebnislisten/ergebnisliste_zuerich.pdf"
daten_muenchen = "daten/daten_muenchen.txt"
daten_freiburg = "daten/daten_freiburg.txt"
daten_zuerich = "daten/daten_zuerich.txt"
alter_min = 2010
alter_max = 1925

def einlesen_muenchen():
    inhalt = ""
    try:
        with pdf.open(dateipfad_muenchen) as file:
           for page in file.pages:
                inhalt += page.extract_text()
    except:
        print(f"Der Dateipfad {dateipfad_muenchen} ist nicht bekannt.\n Bitte diesen dementsprechend abaendern")
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
            if len(schluessel) > 5:
                schluessel = schluessel[:4]         # Ab Startnummer 1.000 Fehlt ein Leerzeichen, deswegen wird die Entfernung hier manuell durchgeführt
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
                elif element.count(":") == 2 and element.count("(") == 0 and element[0].isdigit() or element.count(":") == 4:
                    if element.count("+") == 1:
                        position = element.find("+")
                        element = element[:position]                                # Ab dem Plus-Zeichen, sämtliche Strings entfernen
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha() and element.isupper()) or (len(element) == 3 and element[0].isalpha() and element[1].isdigit() and element[2].isdigit()):                   
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
    key_zaehler = 0
    daten = daten.split("\n")                       # Daten nach Zeilen sortieren
    for zeile in daten:                             # Auslesen der Daten
        daten_liste = []
        if zeile.strip():                       
            zeile = zeile.split()
            schluessel = zeile[0]                   # Platzierung als Schlüssel
            schluessel = schluessel.replace(".", "")
            try:
                schluessel_int = int(schluessel)
                key_zaehler += 1
            except:
                continue
            for element in zeile:                   # Restliche Daten ermitteln
                if len(element) == 4 and element.isdigit():
                    jahrgang = element
                elif element.count(":") == 2:
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha() and element.islower()):                   
                        geschlecht = element
            try:                                    # Entfernen von fälschlicherweise analysierten Daten
                jahrgang_int = int(jahrgang)
                if jahrgang_int > alter_min or jahrgang_int < alter_max:
                    key_zaehler -= 1                # key_zaehler für nicht verwendete Daten im Dictionary zurücksetzen
                    continue
            except:
                continue
            daten_liste.append(zielzeit)            # Daten in ein Dictionary zur Weiterverarbeitung speichern
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append("u")                 # Nationen als undefined setzen
            dictionary_freiburg[key_zaehler] = daten_liste
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
    key_zaehler = 0
    daten = daten.split("\n")                       # Daten nach Zeilen sortieren
    for zeile in daten:                             # Auslesen der Daten
        daten_liste = []
        if zeile.strip():                       
            zeile = zeile.split()
            schluessel = zeile[0]                   # Platzierung als Schlüssel
            if len(schluessel) > 5:
                schluessel = schluessel[:4]         # Ab Startnummer 1.000 Fehlt ein Leerzeichen, deswegen wird die Entfernung hier manuell durchgeführt
            schluessel = schluessel.replace(".", "")
            try:
                schluessel_int = int(schluessel)    # Aufgrund der Sortierung nach Altersklasse werden hierdurch die DNF- sowie DNS-Teilnehmer gefiltert und anschließend ein entsprechender Key für das Dictionary übergeben
                key_zaehler += 1
            except:
                continue
            for element in zeile:                   # Restliche Daten ermitteln
                if len(element) == 4 and element.isdigit() and count != 1:
                    jahrgang = element
                elif len(element) == 3 and element.isalpha() and element.isupper():
                    nation = element
                elif element.count(":") == 2:
                    zielzeit = element
                elif (len(element) == 1 and element.isalpha() and element.isupper()):                   
                    geschlecht = element
                count += 1                          # Hilsvariable zum Bestimmmen des Jahrgangs
            try:                                    # Entfernen von fälschlicherweise analysierten Daten
                jahrgang_int = int(jahrgang)
                if jahrgang_int > alter_min or jahrgang_int < alter_max:
                    key_zaehler -= 1                # key_zaehler für nicht verwendete Daten im Dictionary zurücksetzen
                    continue
            except:
                continue
            daten_liste.append(zielzeit)            # Daten in ein Dictionary zur Weiterverarbeitung speichern
            daten_liste.append(jahrgang)
            daten_liste.append(geschlecht)
            daten_liste.append(nation)
            dictionary_zuerich[key_zaehler] = daten_liste
            count = 0                               # Zurücksetzen der Hilfsvariable
    return dictionary_zuerich

def concept_muenchen():
    daten_muenchen = einlesen_muenchen()
    dictionary_muenchen = daten_analyse_muenchen(daten_muenchen)
    return dictionary_muenchen

def concept_freiburg():
    daten_freiburg = einlesen_freiburg()
    dictionary_freiburg = daten_analyse_freiburg(daten_freiburg)
    return dictionary_freiburg

def concept_zuerich():
    daten_zuerich = einlesen_zuerich()
    dictionary_zuerich = daten_analyse_zuerich(daten_zuerich)
    return dictionary_zuerich

def daten_speichern(dictionary_muenchen, dictionary_freiburg, dictionary_zuerich):                          # Daten in entsprechende Datei speichern
    with open(daten_muenchen, "w") as file:
        for schluessel, element in dictionary_muenchen.items():                                             # Dictionary mit Keys und Elementen entsprechend durch iterieren
            file.write(f"{str(schluessel)}: {str(element)}\n")
        file.close()
    with open(daten_freiburg, "w") as file:
        for schluessel, element in dictionary_freiburg.items():
            file.write(f"{str(schluessel)}: {str(element)}\n")
        file.close()
    with open(daten_zuerich, "w") as file:
        for schluessel, element in dictionary_zuerich.items():
            file.write(f"{str(schluessel)}: {str(element)}\n")
        file.close()

def main_daten_select():
    results_dictionary = {}                         # Zwischenspeicher für Rückgabewerte der Thread-Funktionen
    dictionary_muenchen = {}
    dictionary_freiburg = {}
    dictionary_zuerich = {}
    def speichern_muenchen():
        results_dictionary["Muenchen"] = concept_muenchen()
    def speichern_freiburg():
        results_dictionary["Freiburg"] = concept_freiburg()
    def speichern_zuerich():
        results_dictionary["Zuerich"] = concept_zuerich()
    thread_muenchen = thread.Thread(target=speichern_muenchen)          # Threads anlegen und starten
    thread_freiburg = thread.Thread(target=speichern_freiburg)
    thread_zuerich = thread.Thread(target=speichern_zuerich)
    thread_muenchen.start()
    thread_freiburg.start()
    thread_zuerich.start()
    thread_muenchen.join()                                                                                        # Auf beenden der jeweiligen Threads warten
    thread_freiburg.join()
    thread_zuerich.join()
    dictionary_muenchen = results_dictionary["Muenchen"]
    dictionary_freiburg = results_dictionary["Freiburg"]
    dictionary_zuerich = results_dictionary["Zuerich"]
    daten_speichern(dictionary_muenchen, dictionary_freiburg, dictionary_zuerich)                                 # Speichern von Daten in entsprechende Dateien

main_daten_select()
