#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[4]:


df = pd.read_csv("/home/raj/Downloads/archive/data.csv")
df.head(5)


# In[5]:


df.tail(5)


# In[6]:


df.dtypes


# In[7]:


df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)


# In[8]:


df.head(5)


# In[9]:


df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG":"MPG-H","city mpg":"MPG-C","MSRP":"price"})
df.head()


# In[10]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[11]:


df.count()


# In[12]:


df = df.drop_duplicates()
df.count()


# In[16]:


print(df.isnull().sum())


# In[17]:


df = df.dropna()    # Dropping the missing values.
df.count()


# In[18]:


print(df.isnull().sum())   # After dropping the values


# In[20]:


sns.boxplot(x=df['price'])


# In[21]:


sns.boxplot(x=df['HP'])


# In[22]:


sns.boxplot(x=df['Cylinders'])


# In[23]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[24]:



df.shape


# In[26]:


df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

df.shape


# In[36]:


df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[32]:


df.head()


# In[39]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[41]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()


# In[ ]:




