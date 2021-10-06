#!/usr/bin/env python
# coding: utf-8

# # Data Analysis
# This module will explore the stage of data analysis using the lens of a bias-aware methodology. We will make use of Jupyter notebooks to aid our exploratory data analysis, in order to understand how social, cognitive, and statistical biases interact and affect downstream stages in the research and innovation lifecycle. However, you do not need to have any experience with Python or Jupyter Notebooks to follow along. 
# 
# Exploratory data analysis is an important stage for hypothesis generation or uncovering possible limitations of the dataset that can arise from missing data, in turn identifying the need for any subsequent augmentation of the dataset to deal with possible class imbalances. However, there are also risks that stem from cognitive biases (e.g. confirmation bias) that can create cascading effects that effect downstream tasks (e.g. model reporting).
# 
# We will look at the following stages of data analysis:
# 
# 1. Importing Data
# 2. Describing the Data
# 3. Analysing the Data
# 4. Querying the Data
# 5. Visualising the Data

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[ ]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);

