#!/usr/bin/env python
# coding: utf-8

# # Data Analysis
# This module will introduce and examine the stage of 'exploratory data analysis'. 
# 
# Rather than focusing on the statistical or technical techniques employed in modern data science though, we will approach this stage with a bias-aware perspective. 
# However, we will make use of Jupyter notebooks—a popular tool in data science—to aid our exploratory data analysis[^jupyter] by visualising some data. 
# You do not need to be familiar with either Python or Jupyter Notebooks if you just want to gain an understanding of how social, cognitive, and statistical biases interact and affect downstream stages in the research and innovation lifecycle. 
# But the code is presented for those who wish to get more "hands-on".
# 
# You can also edit this code in an interactive Jupyter notebook: 
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chrisdburr/turing-commons/master?labpath=https%3A%2F%2Fgithub.com%2Fchrisdburr%2Fturing-commons%2Fblob%2Fmaster%2Fguidebooks%2Frri%2Fchapter4%2Fproject_design%2Fdata_analysis.ipynb)
# 
# ## What is Exploratory Data Analysis?
# 
# Exploratory data analysis is a crucial stage in the project lifecycle. It is where a number of techniques are employed for the purpose of gaining a better understanding of the dataset and any relationships that exist between the relevant variables. Among other things, this could mean,
# 
# - Describing the dataset and important variables
# - Cleaning the dataset
# - Identifying missing data and outliers, and deciding how to handle them
# - Provisional analysis of any relationships between variables
# - Uncovering possible limitations of the dataset (e.g. class imbalances) that could affect the project
# 
# We will cover each of these sub-stages of EDA briefly, but to reiterate, our primary focus in this section is on the risks and challenges that stem from a variety of biases that can cause cascading issues that affect downstream tasks (e.g. model training).
# 
# ## COVID-19 Hospital Data
# 
# For the purpose of this section we have created a synthetic dataset that contains X records for fictional patients who were triaged (and possibly admitted) to a single hospital for treatment of COVID-19. 
# 
# The dataset has been designed with this pedagogical task in mind. 
# Therefore, although we relied upon plausible assumptions when developing our generative model, the data are not intended to be fully representative of actual patients. Our methodology for generating this dataset can be [found here](Synthetic_data_generation.ipynb).
# 
# ### Importing Data
# 
# First of all, we need to import our data and the software packages that we will use to describe, analyse, and visualise the data. 
# The following lines of code achieve this by importing a series of software packages and then loading a csv file `covid_patients_syn_data.csv` into a DataFrame `df` using the `pd.read_csv` command from the Pandas package.

# In[1]:


# The following lines import necessary packages and renames them 

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# This line imports data from a csv file 

df = pd.read_csv('covid_patients_syn_data.csv')


# ### Describing the Data
# 
# Once we have imported our data, we will then want to identify what variables there are, what their typical values are, and also assess a variety of other summary statistics. 
# We can use several commands to help us describe our dataset and get a quick overview.
# 
# First, we can use the `shape` attribute to list the number of rows and columns in our dataset.
# The output (30000, 11) means that there are 3000 rows and 12 columns.
# 

# In[ ]:


df.shape


# Second, we can use the `head` attribute to return the first 5 rows of our dataset, which can be useful if you want to see a small sample of values for each variable.

# In[ ]:


df.head() 


# Third, we can use the `columns` attribute to list all the names all of the columns in our dataset. 
# This is helpful if you want to quickly see which variables you will have access to during your analysis.

# In[ ]:


df.columns


# Finally, if we want to see how many *unique* values there are for each of the variables, we can use the `nunique` attribute (i.e., number (n) of unique values).
# For example, in the ethnicity column there are 5 different values, which align with the formal list used by Public Health England in a report on the [Disparities in the risk and outcomes of COVID-19](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/908434/Disparities_in_the_risk_and_outcomes_of_COVID_August_2020_update.pdf)—this report was used as the basis for generating our synthetic data.

# In[ ]:


df.nunique(axis=0)


# These commands can be helpful for describing some basic aspects of our dataset. But what about more useful statistical information?
# For that we have the `describe` attribute, which returns the numeric values for `count`, `mean`, `standard deviation`, `min`, and `max`.
# The code after the brackets (`apply(lambda s: s.apply(lambda x: format(x, 'f'))` helps improve readability.)

# In[ ]:


df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))


# ### Cleaning the Data
# 
# #### Removing Unnecessary Variables
# 
# Our dataset has been created for this specific task, so there isn't much cleaning that is required.
# Datasets that are downloaded from public repositories may not be so well structured, and will likely require tidying up. 
# For instance, there may be redundant columns that are not needed, such as the `site_id` column for our dataset, which is the same for all values due to the data being collected from a single hospital site (`UHJ_43643`).
# These can be easily removed with the `drop` function.

# In[ ]:


df_cleaned = df.drop(['site_id'], axis=1)
df_cleaned.head()


# #### Removing Outliers
# 
# It is also possible that there may be some outliers that are probably the result of human mistakes in recording, such as the `X` value in the `Y` column.
# It's probably a safe assumption to assume that this is a mistake!

# In[ ]:


df_cleaned.hist("height") 


# #### Handling Missing Data
# 
# However, one of the biggest challenges with cleaning datasets is choosing how to handle missing data. 
# As you can see from the following lines of code, there are `X` columns with missing data, which are represented in our datasets using the `null` value.
# 
# <!-- This section needs to have something about how simply removing rows with null values or trying to impute the likelihood of a M or F based on the other variables may exacerbate representation bias. -->
# 

# ### Analysing the Data
# 
# <!-- This section needs to add some useful illustrations of how Python can help you identify and understand correlations between variables in your dataset, and help document your exploratory data analysis method by using Jupyter Notebooks. -->

# In[ ]:


# The following lines return a correlation matrix, for the cleaned dataframe, using the seaborn package
corr = df.corr()# plot the heatmap

sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))


# ### Visualising the Data
# 
# <!-- This section should show how including people who died in care homes would affect the correlation between age and one or more of the outcomes. This will be used to help support the missing data narrative. -->
