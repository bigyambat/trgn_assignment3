#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import sys

#Tells which specific column to select

if "-f" in sys.argv[1]:
    n = sys.argv[1]
    column_number= int(n[2])
else: column_number = 2

# print(column_number)

#Creation of Histogram based on specific column
df = pd.read_csv(sys.argv[2], sep=",", header=0)
df.head(1)
col_name = df.columns[column_number]
ax =df.loc[:,col_name]

final_plot = ax.plot.hist()
plt.savefig('histogram_figure.png')
