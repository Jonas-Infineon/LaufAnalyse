import daten_Select as data_collect
import dataVisualisierung as data_visualize

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
    visualize_muenchen()
    visualize_freiburg()
    visualize_zuerich()

def visualize_muenchen():
    data_visualize.visu("daten/daten_muenchen.txt", "Muenchen")

def visualize_freiburg():
    data_visualize.visu("daten/daten_freiburg.txt", "Freiburg")

def visualize_zuerich():
    data_visualize.visu("daten/daten_zuerich.txt", "Zuerich")


main()
    