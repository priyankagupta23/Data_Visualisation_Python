# -*- coding: utf-8 -*-
"""SwarmPlot_SalesVisualisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BQyPzQiy6LSuHUkPd7DOY8xNkq8mezx1
"""

import numpy as np
import pandas as pd
import seaborn as sns

sales = pd.read_csv('sales_data_sample.csv', encoding = 'unicode_escape')

sales.info()

sales.head()

sns.jointplot('PRICEEACH', 'SALES', data = sales);

sns.jointplot('PRICEEACH', 'SALES', data = sales, kind = 'kde')

sns.swarmplot(sales.SALES)

sns.swarmplot(sales.PRICEEACH)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15,8))
sns.swarmplot(x = 'COUNTRY', y = 'SALES', data = sales);

sns.swarmplot(x = 'DEALSIZE', y = 'SALES', data = sales);

fig = plt.figure(figsize = (12, 6))
sns.swarmplot(x = 'PRODUCTLINE', y = 'SALES', data = sales)
plt.show();