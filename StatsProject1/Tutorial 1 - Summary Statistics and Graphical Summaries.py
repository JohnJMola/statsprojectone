#!/usr/bin/env python
# coding: utf-8

# # Tutorial 1 - Summary Statistics and Graphical Summaries

# ## Getting Started - Importing Libraries

# In order to use Python in order to work with data, we need to first tell Python that we wish to make certain tools available to us. In order to do that, we need to import some libraries. 

# In[52]:


# Allows us to create Data Frames.
import pandas as pd

# Stops matplotlib from opening a new window for our plots. 
get_ipython().run_line_magic('matplotlib', 'inline')

# Imports plotting functionality.
import matplotlib.pyplot as plt

# Imports the ability to calculate statistics.
import numpy as np


# ## Summary Statistics

# Before we start importing data, we are going to play around with the basic functionality of our statistics using a list. 

# In[53]:


# This is a list of commute times collected from various students. 
commute = [15, 17, 17, 18, 19, 19, 20, 20, 21, 21, 21, 22, 23, 24, 26, 26, 31, 36, 38]


# At this point, we can calculate things like mean, standard deviation, and variance.

# In[54]:


# This is the mean of our list. 
np.mean(commute)


# In[55]:


# This is the POPULATION standard deviation.
np.std(commute) 


# In[56]:


# This is the SAMPLE standard deviation. 
# np.std() defaults to population standard deviation. For sample SD, set ddof = 1.
np.std(commute, ddof = 1) 


# In[57]:


# This is the POPULATION variance. 
np.var(commute)


# In[58]:


# This is the SAMPLE variance. 
# np.var() defaults to population variance. For sample variance, set ddof = 1.
np.var(commute, ddof = 1)


# We can also determine the length of our list, as well as our five-number summary.

# In[59]:


# Calculates the sample size.
len(commute)


# In[60]:


# This computes the median.
np.median(commute)


# In[61]:


# This computes the quartiles, minimum, and maximum for our list.
quartiles = np.percentile(commute, [25, 50, 75])
commute_min, commute_max = np.min(commute), np.max(commute)
print('Min: ', commute_min)
print('Q1: ', quartiles[0])
print('Q2: ', quartiles[1])
print('Q3: ', quartiles[2])
print('Max: ', commute_max)


# In[62]:


sixty_third = np.percentile(commute, 63)
print('63rd Percentile: ', sixty_third)


# ## Importing Data

# Without knowing how to import data, knowing how to calculate the statistics will only get us so far. In order for us to import data, we must know how to direct our program to the file we wish to import. Ask Mr. Smith if you are unsure how to do this when reviewing later.

# In[63]:


# Imports our data from "The National Longitudinal Study 
# of Adolescent to Adult Health". More information at https://www.cpc.unc.edu/projects/addhealth
df = pd.read_csv('data/add_health_data.csv', index_col=None, encoding='utf-8')


# In[64]:


# Shows the first ten entries of the data frame. This is useful to gain a sense of what your data looks like. 
df.head(10)


# Having a data frame provides us with some extra perks in Python, allowing us to quickly determine frequencies and find the mean, standard deviation, and the five-number summary.

# In[65]:


# This tells you all unique entries in the BIO_SEX column.
df.BIO_SEX.unique()


# In[66]:


# This determines the frequency for each category.  
df.BIO_SEX.value_counts()


# In[67]:


# We notice that we don't want to include the value of 6, since it is a non-reply. 
# This is how we can filter out rows that contain a specific value in a specific column.
df = df[df.BIO_SEX != 6]
df.BIO_SEX.value_counts()


# In[68]:


# For data frames, df.COLUMN_NAME.describe() will tell you the count, mean, standard deviation, and 
# five-number summary for COLUMN_NAME. 
df['BIO_SEX'].describe()
# It is worth noting that since we understand these numbers represent categorical data, it does not 
# make much sense to compute these things. However, this is a demonstration that we could if necessary.


# In[69]:


# Notice that before, we replaced our data frame with a filtered version.
# This will import the original data set back for us. 
df = pd.read_csv('data/add_health_data.csv', index_col=None, encoding='utf-8')
# .describe() also works for non-numeric data, although it will only give us relevant information.
df.agew1.describe()


# In[70]:


# Since 'agew1' is a column that should give us the age of the individuals, it should be numeric. 
# However, it seems to have been imported as a non-numeric type of data (see above). 
# This code will turn our column into numeric information. 
columns_to_change = {'agew1'}
for col in columns_to_change:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# In[71]:


# Now when we run the .describe() command on 'agew1', we obtain the mean, standard deviation, and 
# five-number summary that we should expect.
df.agew1.describe()


# ## Graphical Summaries

# ### Bar Plots

# In[72]:


categories = df.BIO_SEX.unique()
amounts = df.BIO_SEX.value_counts()
axis_space = np.arange(len(categories))

plt.bar(axis_space, amounts, align = 'center', alpha = 0.5)
plt.xticks(axis_space, categories)
plt.ylabel('Total Respondents')
plt.title('Biological Sex Amounts')
plt.show()


# In[73]:


categories = df.BIO_SEX.unique()
amounts = df.BIO_SEX.value_counts()
axis_space = np.arange(len(categories))

plt.barh(axis_space, amounts, align = 'center', alpha = 0.5)
plt.yticks(axis_space, categories)
plt.xlabel('Total Respondents')
plt.title('Biological Sex Amounts')
plt.show()


# ### Pie Charts

# In[74]:


labels = df.BIO_SEX.unique()
sizes = df.BIO_SEX.value_counts()
colors = ['gold', 'lightcoral', 'lightskyblue']

# You can include this code instead of the following two lines containing 'patches' if you prefer to have your 
# labels on the wedges of the chart.
explode = (0.1, 0, 0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

#patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90) # Remove if alternate code
#plt.legend(patches, labels, loc="best") #Remove if alternate code

plt.axis('equal')
plt.show()


# ### Box Plots

# In[75]:


plt.boxplot(commute);


# In[76]:


plt.boxplot(commute, vert=False);


# ### Time-series Plot

# In[77]:


dji = pd.read_csv('data/DJI.csv')


# In[78]:


dji.head()


# In[79]:


import datetime

x = dji.Date
y = dji.Open

plt.xlabel('Date')
plt.ylabel('Opening Price')
plt.title('DJI Opening Price from 10/1/2014 to 9/1/2019')
plt.plot(x,y)
# Here, the numbers indicate the position from left to right that each label should be at.
# The words after indicate what to display at each label.
# Since this is monthly data, we can count by 12s to place our labels once each year. 
plt.xticks([0, 12, 24, 36, 48, 59], ('Oct 2014', 'Oct 2015', 'Oct 2016', 'Oct 2017', 'Oct 2018', 'Sept 2019'))
plt.show()


# In[ ]:




