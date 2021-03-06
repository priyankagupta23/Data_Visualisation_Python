# -*- coding: utf-8 -*-
"""Line_Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w4quqvhVs7-NYxZ_XiFg5xfhxSLvsHpA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Suicides in India 2001-2012.csv')

df.head()

sns.lineplot(x='Year', y='Total', data=df);

sns.lineplot(x='Year', y='Total', hue='Gender', data=df);

fig = plt.gcf();
fig.set_size_inches(15,6);
sns.lineplot(x='Year', y='Total', hue='Age_group', data=df);

sns.lineplot(x='Year', y='Total', hue='State', size='Gender', style='Age_group', data=df);
plt.legend(bbox_to_anchor=(1.05,1));

x = np.random.rand(10)

y = x * x

sns.lineplot(x, y);