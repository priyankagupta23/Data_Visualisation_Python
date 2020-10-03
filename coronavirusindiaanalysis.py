# -*- coding: utf-8 -*-
"""CoronaVirusIndiaAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L6j4V4guPhwPLKWrCwRkoOwroTY5OrO

###Import Libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns

"""###URL for corona data state wise for India"""

url = 'https://api.covid19india.org/states_daily.json'

"""###Reading the JSON data into dataframe"""

import urllib.request

urllib.request.urlretrieve(url, 'data.json')

covid = pd.read_json('data.json')

covid

import json

with open('data.json') as f:
    data = json.load(f)
#data

type(data)

data.keys()

data = data['states_daily']

#data

df = pd.json_normalize(data)

df.head()

df.info()

"""###Converting the date column into timestamp"""

type(df.date[0])

df.date = pd.to_datetime(df.date)

type(df.date[0])

df.status == 'Confirmed'

"""###Subsetting the dataframe to only confirmed cases"""

df[df.status == 'Confirmed']

df = df[df.status == 'Confirmed']

df.drop('status', axis=1, inplace=True)

"""###Setting date as the index"""

df.set_index('date', inplace=True)

df.head()

"""###Converting the values from object to numeric"""

df = df.apply(pd.to_numeric)

df.info()

df.tail()

"""###Highlighting the max value of each state"""

df.tail().style.highlight_max(color='red')

"""###Defining a method to make the maximum value as bold"""

def bold_max(x):
    is_max = (x == x.max())
    return ['font-weight: bold' if y else '' for y in is_max]

df.tail().style.apply(bold_max)

"""###Finding the maximum value in each row"""

df.tail().style.highlight_max(color='red', axis=1)

"""###Styling the table with color map"""

df.tail().style.background_gradient(cmap='Reds')

"""###Checking the bar graph for 3 most infected states"""

df.tail()[['mh','dl','tn']].style.bar()

"""###Histogram for the state of Maharashtra"""

sns.distplot(df[['mh']])

"""#Analysis of number of positive cases as compared to number of tests done"""

url2 = 'https://api.covid19india.org/state_test_data.json'

import urllib.request

import json

import pandas as pd

urllib.request.urlretrieve(url2, 'data.json')

covid = pd.read_json('data.json')

covid

type(covid['states_tested_data'][0])

covid['states_tested_data'][0]

with open('data.json') as f:
    data = json.load(f)

#data

type(data)

data.keys()

data = data['states_tested_data']

type(data)

type(data[0])

df = pd.json_normalize(data)

df.head()

df = df[['positive','state','totaltested','updatedon']]

df.head()

covid = df.set_index('updatedon')

covid.head()

type(covid.index[0])

type(covid['positive'][0])

covid[['positive','totaltested']] = covid[['positive','totaltested']].apply(pd.to_numeric)

covid.head()

import matplotlib.pyplot as plt
import seaborn as sns

"""##Graph of positive cases in Delhi"""

sns.barplot(x = covid[covid['state'] == 'Delhi'].index, y = covid[covid['state'] == 'Delhi']['positive'])

covid['%positive/tested'] = covid['positive']/covid['totaltested']

"""##Graph of ratio of positive cases to number of tests done in Delhi"""

#plt.figure(figsize=(15,8))
sns.barplot(x = covid[covid['state'] == 'Delhi'].index, y = covid[covid['state'] == 'Delhi']['%positive/tested'])

"""As we can see that number of positive cases rose in Delhi but the number of positive cases over number of tests done are reducing which means lesser proportion of people getting tested are coming positive

##Graph of proportion of people tested positive over the number of people tested in Maharashtra
"""

#plt.figure(figsize=(12,6))
sns.barplot(x = covid[covid['state'] == 'Maharashtra'].index, y = covid[covid['state'] == 'Maharashtra']['%positive/tested'])

covid.head()

covid.head()

covid_state = covid.groupby('state')[['positive','totaltested']].sum()

covid_state.head()

plt.figure(figsize=(12,6))
sns.barplot(x = covid_state.index, y = covid_state['positive'])

covid.info()

covid.to_excel("covid.xlsx")