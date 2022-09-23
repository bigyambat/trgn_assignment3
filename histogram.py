#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import sys

#Tells which specific column to select
if sys.argv[:1] == "-f":
    n = str((column_selection[2]))
print(n)

#Creation of Histogram based on specific column
df = pd.read_csv('expres.anal.tsv', sep="\t", header=0)
df.head(1)
data_frame = pd.DataFrame(df)
# columns = [1,2,3,4,5,6,7,8,9,10]
data_frame=data_frame['logFC']
ax = df.plot.hist()
