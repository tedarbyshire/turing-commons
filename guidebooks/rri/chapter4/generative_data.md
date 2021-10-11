# Notes on Data Analysis Activity

## Goals/Objectives

- To introduce participants, many of whom will not be data scientists, to some of the issues that arise during the exploratory data analysis (EDA) stage
- To discuss how a range of biases can affect the process of EDA
- To visualise the effects of bias on data analysis

## Case Study

A research team are exploring whether risk of deterioration from COVID-19 can be predicted during admission and triaging of patients. They have a dataset collected over the course of a couple of months from a single hospital. The dataset includes a variety of demographic and physiological parameters for each patient and indicates whether/when they deteriorated and if they required emergency invasive ventilation.

### Features

- (Pseudonymous) NHS number
  - This can just be a random string of digits (e.g. #186357)
- Age (range, not lower than 80)
  - 18–30
  - 31-40
  - 41–50
  - 51–60
  - 61–70
  - 71-80
  - 80+
- Sex
- Ethicity (official distributions: https://www.ethnicity-facts-figures.service.gov.uk/uk-population-by-ethnicity/national-and-regional-populations/population-of-england-and-wales/latest / COVID deaths by ethnicity: https://www.gov.uk/government/publications/covid-19-reported-sars-cov-2-deaths-in-england/covid-19-confirmed-deaths-in-england-report)
  - White 
    - English, Welsh, Scottish, Northern Irish or British
    - Irish
    - Gypsy or Irish Traveller
    - Any other White background
  - Mixed or Multiple ethnic groups
    - White and Black Caribbean
    - White and Black African
    - White and Asian
    - Any other Mixed or Multiple ethnic background
  - Asian or Asian British
    - Indian
    - Pakistani
    - Bangladeshi
    - Chinese
    - Any other Asian background
  - Black, African, Caribbean or Black British
    - African
    - Caribbean
    - Any other Black, African or Caribbean background
  - Other ethnic group
    - Arab
    - Any other ethnic group
- BMI*
- Temperature
- Heart Rate
- Received Respiratory Support (e.g. CPAP)*
- Outcomes
  - Received invasive ventilation (yes/no)
  - Clinical Outcome (survived/died)

### Biases to show

- Missing data bias
  - One group should be missing from the data (probably elderly people who would not have made it to hospital and, therefore, not been triaged or seen healthcare professional)
- 