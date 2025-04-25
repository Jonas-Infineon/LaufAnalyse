import daten_Select as data_collect
import dataVisualisierung as data_visualize
import dataVis as general_visualize

daten_muenchen = "daten/daten_muenchen.txt"
daten_freiburg = "daten/daten_freiburg.txt"
daten_zuerich = "daten/daten_zuerich.txt"

def main():
    check = 1
    while check:
        try:
            entscheidung = int(input("Bitte eingeben, ob Daten neu eingelesen werden sollen (entspricht 0) oder bestehende Daten verwendet werden sollen (entspricht 1): "))
            if entscheidung:
                check = 0
            elif entscheidung == 0:
                data_collect.main_daten_select()
                check = 0
        except:
            print("Ungueltige Eingabe. Bitte erneut eingeben")
    # Anzeigen der einzelnen Analysen
    visualize_muenchen()
    visualize_freiburg()
    visualize_zuerich()
    # Anzeigen der Gesamtanalyse
    visualize_general()

def visualize_muenchen():
    data_visualize.visu(daten_muenchen, "Muenchen")

def visualize_freiburg():
    data_visualize.visu(daten_freiburg, "Freiburg")

def visualize_zuerich():
    data_visualize.visu(daten_zuerich, "Zuerich")

def visualize_general():
    general_visualize.general_data_visualize(daten_muenchen, daten_freiburg, daten_zuerich)

main()
    