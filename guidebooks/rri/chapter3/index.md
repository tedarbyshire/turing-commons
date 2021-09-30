# Responsible Project Design

## Project Planning and Problem Formulation

<!-- - Setting up a process for responsible data management
- Stakeholder identification and engagement plan -->

In terms of the social understanding of problem formulation, consider the following:

> An AI system that is designed to diagnose diseases based on relevant symptoms or indicators (e.g., biomarkers) would likely develop a problem formulation that assumes that any "disease" ought to be identified, regardless of whether the individual could afford the treatment, whether such a treatment is even available, or whether the individual would self-identify as "ill" or as a patient. Such assumptions are to be expected from the perspective of societies with highly-developed technical medical systems, but are more exclusionary of standpoints that emphasis preventative lifestyle approaches over reactive medical interventions (von Schomberg, 2011)

<!-- #### Activity 1: Breakout Discussions
- How much information should be shared with research subjects to ensure "informed consent"?
- When is it okay to use/scrape publicly available data?

## Data Extraction and Procurement
%%- Respecting rights of data subjects
- Reusing data—what do you need to know about the provenance of a dataset?%%

## Data Analysis
%%- Identifying the effects of social, statistical, and cognitive biases%%

%%This module will explore the stage of data analysis using the lens of a bias-aware methodology. We will make use of Jupyter notebooks to aid our exploratory data analysis, in order to understand how social, cognitive, and statistical biases interact and affect downstream stages in the research and innovation lifecycle.%% -->

%%## Learning Objective
The objective of this module is to understand how bias affects exploratory data analysis, and what ought to be done to minimise the effect of these biases on downstream stages. %%

### Exploring Data

This section will look at the following stages of exploratory data analysis:

1. Importing Data
2. Describing the Data
3. Analysing the Data
4. Querying the Data
5. Visualising the Data

#### Importing Data

We will be using the Pandas library in Python for this module.

```python
# Import the `pandas` library as `pd`
import pandas as pd

# Load the data into a dataframe with `read_csv()`, treating the first row as data rather than as headersimport 
df = pd.read_csv("...", header=None)

# Print out `digits`
print(df)
```
