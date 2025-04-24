import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

import Dictionary as dc

time_ls = []
age_ls = []

for i in range(1, len(dc.dic) + 1):
    try:
        now = dc.dic[i][0]
        h, m, s = map(int, now.split(":"))
        total_time = h * 3600 + m * 60 + s
        time_ls.append(total_time)

        age = 2025 - int(dc.dic[i][1])
        age_ls.append(age)
    except Exception as e:
        print(f"Error processing entry {i}: {e}")
        print(f"Entry content: {dc.dic[i]}")

print(f"Min age: {min(age_ls)}, Max age: {max(age_ls)}")

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


plt.figure(figsize=(10, 6))
plt.plot(ages, avg_time_values, 'o-', linewidth=2)

def format_time(sec):
    h = int(sec) // 3600
    m = (int(sec) % 3600) // 60
    s = int(sec) % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def time_formatter(x, pos):
    return format_time(x)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))

plt.show()