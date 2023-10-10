from quickSort import quick_sort
from mergeSort import merge_sort
from insertionSort import insertion_sort

import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

df = pd.read_csv('results.csv')

random = df['random']
ordered = df['ordered']
evil3 = df['evil3']

input_sizes = df['N']

#create best-fitted line of degree 2
coeffs = np.polyfit(input_sizes, evil3, 2)
fitted_curve = np.poly1d(coeffs)
x_smooth = np.linspace(min(input_sizes), max(input_sizes), 100)
y_smooth = fitted_curve(x_smooth)


plt.figure(figsize=(10, 6))
plt.plot(input_sizes, random, label='random', color = '#00BFFF')
#plt.plot(input_sizes, ordered, label='ordered', color = '#00BFFF')
plt.plot(input_sizes, evil3, label='evil', color = '#104E8B')
plt.plot(input_sizes, y_smooth,label = "O(n^2)",linewidth=2.5, color = 'Red')

plt.xlabel('Size of Input Sequence')
plt.ylabel('Average Runtime (seconds)')
plt.title('QuickSort: Evil v.s. Random sequences',loc = "left")
plt.legend()


plt.grid(True)
plt.show()