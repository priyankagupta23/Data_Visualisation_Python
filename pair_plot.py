# -*- coding: utf-8 -*-
"""Pair_Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FjmJ3zhXcXTw3i6oHCUYDYedEg7w6rPz
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('2015.csv')

df.head()

sns.jointplot(x = 'Economy (GDP per Capita)', y = 'Happiness Score', data = df);

sns.jointplot(x = 'Generosity', y = 'Happiness Score', data = df);

sns.pairplot(df);

df.Region.unique()

df['Status'] = df['Region'].apply(lambda x: 'Developed' if x in ['Western Europe','North America','Australia and New Zealand',
                                                                 'Central and Eastern Europe','Eastern Asia'] else 'Undeveloped')

df.head()

sns.pairplot(df, hue = 'Status');

sns.pairplot(df, hue = 'Status', corner = True);