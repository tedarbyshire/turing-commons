#!/usr/bin/env python
# coding: utf-8

# # Data Analysis
# This module will introduce and examine the stage of 'exploratory data analysis'. 
# 
# Rather than focusing on the statistical or technical techniques employed in modern data science though, we will approach this stage with a bias-aware perspective. However, we will make use of Jupyter notebooks—a popular tool in data science—to aid our exploratory data analysis[^jupyter] by visualising some data. You do not need to be familiar with either Python or Jupyter Notebooks if you just want to gain an understanding of how social, cognitive, and statistical biases interact and affect downstream stages in the research and innovation lifecycle. But the code is presented for those who wish to get more "hands-on".
# 
# ## What is Exploratory Data Analysis?
# 
# Exploratory data analysis is a crucial stage in the project lifecycle. It is where a number of techniques are employed for the purpose of gaining a better understanding of the dataset and any relationships that exist between the relevant variables. Among other things, this could mean,
# 
# - Describing the dataset and important variables
# - Identifying missing data and outliers, and deciding how to handle them
# - Cleaning the dataset
# - Provisional analysis of any relationships between variables
# - Uncovering possible limitations of the dataset (e.g. class imbalances) that could affect the project
# 
# We will cover each of these sub-stages of EDA briefly, but to reiterate, our primary focus in this section is on the risks and challenges that stem from a variety of biases that can cause cascading issues that affect downstream tasks (e.g. model training).
# 
# ## COVID-19 Hopsital Data
# 
# For the purpose of this section we have created a synthetic dataset that contains X records for fictional patients who were triaged (and possibly admitted) to a single hospital for treatment of COVID-19. 
# 
# The dataset has been designed with this pedagogical task in mind. Therefore, although we relied upon plausible assumptions when developing our generative model, the data are not intended to be fully representative of actual patients. Our methodology for generating this dataset can be found here.
# 
# ### Importing Data
# 
# First of all, we need to import our data and the software packages that we will use to describe, analyse, and visualise the data. The following lines of code achieve this, and also loads our data into a DataFrame using the Pandas package:

# In[1]:


# The following lines import necessary packages

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# This line imports data from a csv file into a DataFrame (df)

df = pd.read_csv('train.csv')


# ### Describing the Data
# 

# In[ ]:


# This line returns information about the number of rows and the number of columns for a dataset.

df.shape


# In[ ]:


# This line returns the first 5 rows of a dataset, which can be useful if you want to see a small sample of values for each variable.

df.head() 


# In[ ]:


# This line returns the name of all of the columns in your dataset. This is helpful if you want to quickly see which variables you will have access to during your analysis.

df.columns


# In[ ]:


# This line returns the number of unique values for each of the variables. For example, in the ethnicity column there are X different values.

df.nunique(axis=0)


# In[ ]:


# This line uses the pandas 'describe()' method to provide a summary of the dataset (formatted for readability). This includes the count, mean, standard deviation, min, and max for numeric variables.

df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))


# ### Cleaning and Querying the Data
# 

# ### Analysing the Data
# 

# In[ ]:


# The following lines return a correlation matrix, for the cleaned dataframe, using the seaborn package
corr = df.corr()# plot the heatmap

sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))


# ### Visualising the Data
