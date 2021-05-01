#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Homework exercises for Week #3
# Task 1
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
# # read in the data and print it
df = pd.read_csv('response.csv', delimiter = ",")
df


# In[6]:


# See data types of each column of the data frame (object is string)
df.dtypes


# In[8]:


# # change min from string to numeric
df['min'] = pd.to_numeric(df['min'], errors = 'coerce')
df


# In[9]:


# make a time variable
df['time'] = df['min']*60 + df.sec
df


# In[8]:


df[0:4]


# In[10]:


# Summary statistics can help us understand the data (and also clean it)
df.describe() # returns for numerical values


# In[12]:


df.describe(include = 'all')  # to overview all type entries


# In[14]:


df.shape # gets number of columns and rows


# In[13]:


df['exp'].value_counts()  # get counts for categorical data


# In[15]:


# Data cleaning
# criterias: seconds should be in [0,60],
# - only one option should be ticked in 'Experience',
# -there should be no missing values,
# - there should be no extreme values (outliers)

df.loc[df['exp'] == 'No']
df.loc[df['exp'] != 'No']
df.loc[df['exp'].isin(['Yes','No'])]
df.loc[~df['exp'].isin(['Yes','No'])]

df['exp'].loc[~df['exp'].isin(['Yes','No'])] = np.nan  # only one option should be ticked in 'Experience',
df.loc[~df['exp'].isin(['Yes','No']),'exp'] = np.nan


# In[19]:


df


# In[79]:


# cor type should be either yes or no
# line 1 need to be fixed
df.loc[df['cor'] == 'No']
df.loc[df['cor'] != 'No']
df.loc[df['cor'].isin(['Yes','No'])]
df.loc[~df['cor'].isin(['Yes','No'])]

df['cor'].loc[~df['cor'].isin(['Yes','No'])] = np.nan  # if value is not Yes or No change it to NaN value
df


# In[83]:


df.loc[df['sec'] > 60]
df.loc[df['sec'] > 60,'sec'] = np.nan  # criterias: seconds should be in [0,60] else change value to NaN
df


# In[25]:


# -there should be no missing values,
df = df.dropna()  # value with NaN should be removed
df


# In[20]:


# Visualization of data can help us understand it
# numeric data
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df.plot(x = 'Unnamed: 0', y = 'time', kind = 'scatter') # scatter plot 
df.plot(x = 'hour', y = 'time', kind = 'scatter')
df.plot(y = 'time', kind = 'density') # density plot


# In[27]:


df['type'].value_counts().plot(kind='bar')


# In[22]:


df.hist(column = 'time', bins = 4)
df.hist(column = 'time', bins = 4, by = 'type') # split by Sudoku type


# In[39]:


# Investigate if the participants in the sudoku experiment were faster doing the Latin letter or 
# the Greek letter sudoku by taking the mean time for each type of sudoku 
df_mean = df.drop(columns=['exp','Unnamed: 0','cor','diff','hour','sec','min'])
df_mean  # we need only type and time column to calculate mean for time 


# In[43]:


# then calculate mean time for each Greek and Latin  sudoku
df_mean_greek = df_mean[df_mean['type'] == 'Greek'].mean()  # calculate mean time for Greek sudoku 
print(df_mean_greek)  # time    368.0
df_mean_latin = df_mean[df_mean['type'] == 'Latin'].mean()   # calculate mean time for Latin sudoku 
print(df_mean_latin)  # time    539.5, latine takes loger time!!


# In[45]:


# Fitting a model

import statsmodels.formula.api as sm

df = df.dropna() # remove all data points with missing values

result = sm.ols(formula="time ~ diff", data=df).fit()
print(result.params)
print(result.summary())


# In[27]:


[method_name for method_name in dir(result) if callable(getattr(result, method_name))] # see which methods are available for this object


# In[34]:


newdata = {'time':[np.nan]*10,
        'diff':list(range(1,11))}
  
# Create DataFrame
newdf = pd.DataFrame(newdata)
newdf
newdf['time'] = result.predict(newdf)


# In[35]:


newdf
newdf.plot(x = 'diff', y = 'time')

# scatter plot with predictions in blue and data in red
ax = plt.subplot(1, 1, 1)
ax.scatter(df['diff'], df['time'], color = "red")


# In[41]:


from patsy import dmatrix
# import statsmodels.api as sm
# Fit a more flexible model
diff_cubic = dmatrix('bs(x, knots=())', {'x': df['diff']})
result_cubic = sm.GLM(df['time'], diff_cubic).fit()


# In[42]:


newdiff_cubic = dmatrix('bs(x, knots=())', {'x': newdf['diff']})


plt.figure()
plt.scatter(x = newdf['diff'], y = result_cubic.predict(newdiff_cubic))

ax = plt.subplot(1, 1, 1)
ax.scatter(df['diff'], df['time'], color = "red")


# In[46]:


result = sm.ols(formula="time ~ type", data=df).fit()
print(result.params)
result = sm.ols(formula="time ~ type + diff", data=df).fit()
print(result.params)


# In[44]:


# Spam detection (example)

df = pd.read_csv('SMSSpamCollection.txt', delimiter = "\t", names=['s','t'])
df.head(4)


# In[167]:


list(df)


# In[168]:


#  To generate the length of the text message and the lenght of the first group of uppercase letters
import re
df['l'] = df['t'].str.len()
df['f'] = df.t.str.extract('([A-Z_]+)')
df['fl'] = df['f'].str.len()
df2 = df.t.str.extractall('([A-Z_]+)')


# In[169]:


df3.index.names = ['name', 'yes']


# In[170]:


df2.index.names = ['text','no']
df2


# In[171]:


df['uc'] = df2.groupby(level=[0]).sum()
df['ucl'] = df['uc'].str.len()


# In[172]:


list(df)


# In[173]:


df['ucr'] = df['ucl'].div(df['l'])
df[['ucr', 'ucl', 'l']]


# In[174]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df[df.l < 200].hist(column = 'l', bins = 50, by = 's')
df[df.ucr < .35].hist(column = 'ucr', bins = 50, by = 's')


# In[52]:


# TASK 3
# Find other features that may be predictive of spam (for instance, as indicated by histograms)
# Finding most frequent words used in spam and ham using wordcloud lib

from wordcloud import WordCloud


# In[53]:


# Checking most repeated words in the spam and in ham messages.
#  using WordCloud library 
sp_words = ' '.join(list(df[df['s'] == 'spam']['t']))
spam = WordCloud(width = 600, height = 500).generate(sp_words)
plt.figure(figsize = (10, 8), facecolor = 'k')
plt.imshow(spam)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()
# From the graph we see the most frequen word in the spam is 'FREE' and secondly 'call'.
# Other more frequent words in the spam includes: text, mobile replay, stop , urgent, claim, prize, now, won, please call, etc.


# In[55]:


# for ham words let's make figere using the wordcloud
ham_words = ' '.join(list(df[df['s'] == 'ham']['t']))
ham = WordCloud(width = 600, height = 500).generate(ham_words)
plt.figure(figsize = (10, 8), facecolor = 'k')
plt.imshow(ham)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()
# where as the most frequent word in the ham(not spam) massages is 'will'. 
# Other most frequent words among others: ok, go, love, know, want call, good, time, day, one, etc. 


# In[ ]:




