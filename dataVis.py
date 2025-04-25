import matplotlib.pyplot as plt
from matplotlib import ticker as ticker
import ast

# Dictionaries für die Daten der drei Städte
dic_freiburg = {}
dic_munchen = {}
dic_zurich = {}

def general_data_visualize(pfad_munchen, pfad_freiburg, pfad_zurich):
    # Funktion zum Einlesen der Datendateien
    def txtToDic(d, c):
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


    # Funktion zur Verarbeitung der Alters- und Zeitdaten
    def processAgeAndTime(dic):
        time_ls = []
        age_ls = []

        for i in range(1, len(dic) + 1):
            try:
                now = dic[i][0]
                h, m, s = map(int, now.split(":"))
                total_time = h * 3600 + m * 60 + s
                time_ls.append(total_time)
                age = 2025 - int(dic[i][1])
                age_ls.append(age)
            except Exception as e:
                print(f"Error processing entry {i}: {e}")
                print(f"Entry content: {dic[i]}")

        age_count = {}
        age_sum_time = {}

        for i in range(len(age_ls)):
            current_age = age_ls[i]

            if current_age not in age_count:
                age_count[current_age] = 0
                age_sum_time[current_age] = 0

            age_count[current_age] += 1
            age_sum_time[current_age] += time_ls[i]

        avg_times = {}
        for age in age_count.keys():
            avg_times[age] = age_sum_time[age] / age_count[age]

        ages = sorted(avg_times.keys())
        avg_time_values = [avg_times[age] for age in ages]
        age_keys = list(age_count.keys())
        age_values = list(age_count.values())

        return ages, avg_time_values, age_keys, age_values


    # Funktion zum Formatieren der Zeit
    def format_time(sec):
        h = int(sec) // 3600
        m = (int(sec) % 3600) // 60
        s = int(sec) % 60
        return f"{h:02d}:{m:02d}:{s:02d}"


    def time_formatter(x, pos):
        return format_time(x)


    # Einlesen der Datendateien
    txtToDic(dic_freiburg, pfad_freiburg)
    txtToDic(dic_munchen, pfad_munchen)
    txtToDic(dic_zurich, pfad_zurich)

    # Verarbeiten der Daten
    ages_freiburg, avg_time_values_freiburg, age_keys_freiburg, age_values_freiburg = processAgeAndTime(dic_freiburg)
    ages_munchen, avg_time_values_munchen, age_keys_munchen, age_values_munchen = processAgeAndTime(dic_munchen)
    ages_zurich, avg_time_values_zurich, age_keys_zurich, age_values_zurich = processAgeAndTime(dic_zurich)

    # Erstellen der Plots
    plt.figure(figsize=(14, 10))

    # Plot 1: Durchschnittliche Zeit pro Alter für alle drei Städte
    plt.subplot(2, 1, 1)
    plt.plot(ages_freiburg, avg_time_values_freiburg, 'o-', linewidth=2, color='blue', label='Freiburg')
    plt.plot(ages_munchen, avg_time_values_munchen, 's-', linewidth=2, color='red', label='München')
    plt.plot(ages_zurich, avg_time_values_zurich, '^-', linewidth=2, color='green', label='Zürich')
    plt.title('Durchschnittliche Zeit pro Alter in verschiedenen Städten', fontsize=14)
    plt.xlabel('Alter', fontsize=12)
    plt.ylabel('Durchschnittliche Zeit (hh:mm:ss)', fontsize=12)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 2: Anzahl der Teilnehmer pro Alter für alle drei Städte
    plt.subplot(2, 1, 2)
    plt.bar([x - 0.2 for x in age_keys_freiburg], age_values_freiburg, width=0.2, color='blue', label='Freiburg')
    plt.bar(age_keys_munchen, age_values_munchen, width=0.2, color='red', label='München')
    plt.bar([x + 0.2 for x in age_keys_zurich], age_values_zurich, width=0.2, color='green', label='Zürich')
    plt.title('Anzahl der Teilnehmer pro Alter in verschiedenen Städten', fontsize=14)
    plt.xlabel('Alter', fontsize=12)
    plt.ylabel('Anzahl der Teilnehmer', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Layout verbessern
    plt.tight_layout()
    print("Grafiken erfolgreich erstellt!")
    plt.show()