#!/usr/bin/env python
# coding: utf-8

# In[252]:


# importing libraries and read data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('recipes.csv')
df.head()


# In[3]:


# checking the shape( number of rows and columns)
df.shape


# In[4]:


# Exploring the data
df.info()


# In[46]:


# 1. Print the names of Columns that have null values
df_null = df.columns[df.isnull().any()].tolist()
df_null


# In[79]:


# 2. Print the recipes with the highest number of aggregateLikes
print(df['aggregateLikes'].idxmax())  #  recipes has the highest number of aggregateLikes (16911)
df['aggregateLikes'][48:52]


# In[86]:


# 3. Handle the missing values of “calcium percent of Daily need”. Sort the resulting DataFrame by id column.
# there are few NaN values and it will not affect the data set if removed
df_cal=df.copy()
df_cal.dropna(subset = ['CalciumpercentOfDailyNeed'], inplace=True)  # rows wtih NaN values are removed
df_cal.sort_values('id', ascending=True)  # the remaining data set is sorted on ascending order by id


# In[87]:


# 4. Delete the columns that have null values == 141, 
# there are two columns and they are removed
df_141 = df.copy()  # copying the dataset
df_141.drop(df_141.columns[df_141.isnull().sum() == 141].tolist(), axis='columns', inplace=True)
df_141.shape  # to check if the number of columns are decreased by two(from 79 to 77)


# In[122]:


# 5.Print the title of the recipes that are vegetarian == TRUE and glutenFree == True
df['title'].loc[(df['vegetarian'] == True) & (df['glutenFree'] == True)]


# In[147]:


# 6. How many vegan recipes are there (Vegan = Vegetarian and dairy free)?
vegan_lists = df[(df['vegetarian'] == True) & (df['dairyFree'] == True)]
number_vegan_recipes = len(vegan_lists)
number_vegan_recipes


# In[185]:


# 7. Compare the average amount of Vitamin B12 for the vegan and non-vegan recipes. 
# How reliable are the results?
df['VitaminB12Amount'].isnull().sum()   # to get number of null value for Vitamin B12 column 57
# Morethan 25% of th recipes have NaN value of Vitamin B12, so the average amount of Vitamin B12
# could not be reliable results
vegan_average = df['VitaminB12Amount'][(df['vegetarian'] == True) & (df['dairyFree'] == True)].mean()
vegan_average  # 0.24333333333333332 average amount of Vitamin B12 for vegan recipes

df_all = df.copy()  # to copy data set
# to get the non vegan recipes, one way is to remove the vegan recipes and then calculate average B12 for non-vegan
vegan_index = df_all[(df['vegetarian'] == True) & (df['dairyFree'] == True)].index # to get index of vegan recipes
non_vegan = df_all.drop(vegan_index)  # to get non-vegan recipes
non_vegan.shape
non_vegan_avarage = non_vegan['VitaminB12Amount'].mean()  # the average amount of Vitamin B12 for non-vegan recipes
non_vegan_avarage  # 1.0345555555555552


# In[254]:


# 8. Compare the average health Score for both types of recipes (vegan vs non-vegan).
 # to calculate average health Score for vegan recipes
vegan_score = df['healthScore'][(df['vegetarian'] == True) & (df['dairyFree'] == True)].mean() 
vegan_score   # 27.724137931034484 is the average health Score for vegan recipes

#  to get  health score for the non-vegan recipes, can be used the non_vegan list from above (7)
non_vegan['healthScore'].mean()  # 18.785123966942148 is health score for non-vegan recipes 


# In[267]:


# 9. Create a new column: "VeganWeek" where you decrease the price of vegan products by 10%, 
# but only if they already cost more than 100.
df_vk = df.copy()
df_vk.loc[df_vk['pricePerServing'] > 100, 'VeganWeek'] = df_vk['pricePerServing'] - df_vk['pricePerServing'] * 0.1  # apply discount
df_vk[['pricePerServing', 'VeganWeek']]


# In[290]:


# 10. Among the non-vegan recipes, find the one requiring most time to prepare. How is it called?
# first we need to remove the vegan recipes then we find maximum value in the 'readyInMinutes' column.
# next we find the index of the reciep with the  maximum time to prepare
# I got the non-vegan recipes list above at 7. and is saved in the verable 'non_vegan'
non_vegan['readyInMinutes'].max()  # 328 is the maximum time to prepare in minutes from non-vegan recipes
non_vegan[non_vegan['readyInMinutes'] == 328].index  # 83 the index of the recipe with max time to prepar
df[['vegetarian','dairyFree', 'readyInMinutes', 'title']][80:96]  # checking


# In[315]:


# 11. Build a model using linear regression on this dataset
# lets take variables with numeric values to build a model 
# and  as inputes/independent values are taken columns CaloriesAmount, FatAmount, CholesterolAmount
# and output value healthScore
df_extract = df[['CaloriesAmount', 'FatAmount', 'CholesterolAmount', 'healthScore']] # extract needed columns
df_extract


# In[298]:


# lets Visualize the relation of the data on graph 
#  CaloriesAmount vs  healthScore
plt.scatter(df_extract['CaloriesAmount'], df_extract['healthScore'], color = 'blue')
plt.xlabel('CaloriesAmount')
plt.ylabel('healthScore')
plt.show()


# In[300]:


# graph of  FatAmount vs  healthScore
plt.scatter(df_extract['FatAmount'], df_extract['healthScore'], color = 'blue')
plt.xlabel('FatAmount')
plt.ylabel('healthScore')
plt.show()


# In[302]:


# graph of  CaloriesAmount vs CholesterolAmount
plt.scatter(df_extract['CaloriesAmount'], df_extract['CholesterolAmount'], color = 'blue')
plt.xlabel('CaloriesAmount')
plt.ylabel('CholesterolAmount')
plt.show()


# In[304]:


# graph of  CaloriesAmount vs  FatAmount
plt.scatter(df_extract['CaloriesAmount'], df_extract['FatAmount'], color = 'blue')
plt.xlabel('CaloriesAmount')
plt.ylabel('FatAmount')
plt.show()


# In[305]:


# FatAmount vs CholesterolAmount graph
plt.scatter(df_extract['FatAmount'], df_extract['CholesterolAmount'], color = 'blue')
plt.xlabel('FatAmount')
plt.ylabel('CholesterolAmount')
plt.show()


# In[321]:


# To divede dataset to train and test
df_train = df_extract[:(int((len(df)*.8)))]
df_test = df_extract[(int((len(df)*.8))):]


# In[325]:


# Asuming independent or input values are CaloriesAmount, FatAmount, CholesterolAmount
# and dependent value healthScore lets train model using linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x_train = np.array(df_train[['CaloriesAmount', 'FatAmount', 'CholesterolAmount']]) # extracting input values
y_train = np.array(df_train['healthScore'])  # output value
model.fit(x_train, y_train)


# In[333]:


print('coefficients: ', model.coef_)
print('Intercept :', model.intercept_)


# In[372]:


# ploting the relation line
plt.plot(x_train, model.coef_ * x_train + model.intercept_, '-y')
plt.ylabel('healthScore')


# In[371]:


# test : lets predict
from sklearn.metrics import r2_score
x_test = np.array(df_test[['CaloriesAmount', 'FatAmount', 'CholesterolAmount']]) # extracting input values
y_test = np.array(df_test['healthScore'])  # output value
y_prediction = model.predict(x_test)
score = r2_score(y_test, y_prediction) # calculating r2_score
score   #  -0.1954497584038235 this indicates the chosen model fits worse than a horizontal line
print('Mean absolute error: %.2f' % np.mean(np.absolute(y_test - y_prediction)))  # Mean absolute error: 23.94 
print('Mean sum of squares(MSE):  %.2f' % np.mean((y_test - y_prediction)**2))  #Mean sum of squares(MSE):  1177.82


# In[364]:


#to visualize the prediction
plt.plot(x_test, model.coef_ * x_test + model.intercept_, '-y')
plt.show()


# In[ ]:




