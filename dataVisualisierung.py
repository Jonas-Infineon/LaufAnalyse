import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
import ast

inhalt = ""
dic = {}

with open("daten/daten_muenchen.txt", "r") as file:
    for zeile in file:
        zeile = zeile.strip()
        if zeile:
            try:
                key, var = zeile.split(":", 1)
                key = key.strip()
                var = ast.literal_eval(var.strip())

                dic[int(key)] = var
            except ValueError as e:
                print(f"Fehler beim Verarbeiten der Zeile: {zeile} -> {e}")
print(dic)

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

ages = sorted(avg_times.keys())
avg_time_values = [avg_times[age] for age in ages]
age_keys = list(age_count.keys())
age_values = list(age_count.values())

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