import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

import Dictionary as dc

time_ls = []
age_ls = []

for i in range(1, len(dc.dic)+1):
    #Zeiten in Sekunden speichern
    now = dc.dic[i][0]
    h,m,s = map(int, now.split(":"))
    total_time = h*3600+m*60+s
    time_ls.append(total_time)

    #Alter speichern
    age_ls.append(2025 - int(dc.dic[i][1]))

def format_time(sec):
    h = int(sec) // 3600
    m = (int(sec) % 3600) // 60
    s = int(sec) % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

plt.plot(age_ls,time_ls)
plt.xlabel("Alter")
plt.ylabel("Zielzeit in Sekunden")
plt.grid(True)
plt.show()