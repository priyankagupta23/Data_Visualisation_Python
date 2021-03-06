# -*- coding: utf-8 -*-
"""Pie_Chart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YjmJJ4hYqjDxXqEdKZ4pocPyzHfaFMsR
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Suicides in India 2001-2012.csv')

df.head()

type_sum = df.groupby('Type')['Total'].sum()
type_sum

fig = plt.figure(figsize=(15,8))
plt.pie(type_sum, labels = type_sum.index, autopct = '%.2f%%');
plt.tight_layout();
plt.show();

cause_sum = df.groupby('Type_code')['Total'].sum()
cause_sum

plt.pie(cause_sum, labels = cause_sum.index, autopct = '%.2f%%');
plt.tight_layout()
plt.show()

gender_sum = df.groupby('Gender')['Total'].sum()
gender_sum

plt.pie(gender_sum, labels = gender_sum.index, autopct = '%.2f%%');
plt.show()