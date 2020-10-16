# -*- coding: utf-8 -*-
"""BarPlot_SuicideAnalysisIndia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFFBTB1MkvVR8udNLBLnUmnNNkzceZra
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

suicide_data = pd.read_csv('/content/Suicides in India 2001-2012.csv')

suicide_data.info()

suicide_data.head()

type_sum = suicide_data.groupby('Type')['Total'].sum()
a = type_sum.sort_values(ascending=False).head(10)
a

fig = plt.figure(figsize=(12,6))
sns.barplot(x = a.index, y = a.values)

b = suicide_data.groupby('State')['Total'].sum().sort_values(ascending=False).head(10)
b

fig = plt.figure(figsize=(12,6))
sns.barplot(x = b.index, y = b.values)

c = suicide_data.groupby(['Year'])['Total'].sum()
c

fig = plt.figure(figsize=(12,6))
sns.barplot(x = c.index, y = c.values)

s = suicide_data.groupby(['State','Type'])['Total'].sum()
s

type_suicide = s[s.groupby('State').transform(lambda x: x == x.max())]

type_suicide

type(type_suicide)

fig = plt.figure(figsize=(12,6))
type_suicide.droplevel(level=1).plot(kind = 'bar')

fig = plt.figure(figsize=(12,6))
type_suicide.droplevel(level=0).groupby('Type').sum().plot(kind = 'bar')

df = suicide_data.groupby(['State','Gender'])['Total'].sum()
df.head()

df = pd.DataFrame(df)
df.head()

df.unstack().plot(kind = 'bar');
plt.tight_layout();
plt.show();

df.unstack().plot(kind = 'bar', stacked = True);
plt.tight_layout();

df2 = df.unstack()
df2.head()

df2.columns

df3 = df2.droplevel(0, axis = 1)
df3.head()

fig = plt.gcf();
fig.set_size_inches(15, 6);
plt.bar(df3.index, df3.Female, color = 'pink')
plt.bar(df3.index, df3.Male, bottom = df3.Female, color = 'blue')
plt.xticks(rotation = 90)
plt.tight_layout()
for i in df3.index :
    y = df3.loc[i].sum()
    x = i
    plt.text(x, y, y, ha = 'center');
plt.show();
