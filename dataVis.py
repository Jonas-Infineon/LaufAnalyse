import matplotlib.pyplot as plt
from matplotlib import ticker as ticker
import ast

pfad_freiburg = "daten/daten_freiburg.txt"
dic_freiburg = {}
dic_freiburg_age_count = {}

pfad_munchen = "daten/daten_muenchen.txt"
dic_munchen = {}
dic_munchen_age_count = {}

pfad_zurich = "daten/daten_zurich.txt"
dic_zurich = {}
dic_zurich_age_count = {}

def txtToDic(d,c):
    with open(c, "r") as file:
        for zeile in file:
            zeile = zeile.strip()
            if zeile:
                try:
                    key, var = zeile.split(":", 1)
                    key = key.strip()
                    var = ast.literal_eval(var.strip())

                    d[int(key)] = var
                except ValueError as e:
                    print(f"Fehler beim Verarbeiten der Zeile: {zeile} -> {e}")

def AgeAndTime():
    print()

def plotter(ages,avg_time_values,age_keys, age_values):
    # Funktion zum Formatieren der Zeit
    def format_time(sec):
        h = int(sec) // 3600
        m = (int(sec) % 3600) // 60
        s = int(sec) % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def time_formatter(x, pos):
        return format_time(x)

    # Erstellen der Subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))  # 2 Zeilen, 1 Spalte

    # Plot 1: Durchschnittliche Zeit pro Alter
    axs[0].plot(ages, avg_time_values, 'o-', linewidth=2, color='blue')
    axs[0].set_title('Durchschnittliche Zeit pro Alter', fontsize=14)
    axs[0].set_xlabel('Alter', fontsize=12)
    axs[0].set_ylabel('Durchschnittliche Zeit (hh:mm:ss)', fontsize=12)
    axs[0].yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))

    # Plot 2: Anzahl der Personen pro Alter
    axs[1].bar(age_keys, age_values, color='orange')
    axs[1].set_title('Anzahl der Personen pro Alter', fontsize=14)
    axs[1].set_xlabel('Alter', fontsize=12)
    axs[1].set_ylabel('Anzahl der Personen', fontsize=12)

    # Layout verbessern
    fig.tight_layout()
    print("Success")
    plt.show()