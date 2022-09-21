#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('expres.anal.csv')
df.head(1)


def column(n):
    df[n].plot(kind='hist')

n = print("What column do you want to make a histogram of? ")
n = column(n)
