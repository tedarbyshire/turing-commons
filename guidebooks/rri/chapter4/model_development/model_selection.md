# Model Selection and Training

This stage determines the model type and structure that will be produced in the next stages.
In some projects, model selection will result in multiple models for the purpose of comparison based on some performance metric (e.g. accuracy).
In other projects, there may be a need to first of all implement a pre-existing set of formal models into code.
The class of relevant models is likely to have been highly constrained by many of the previous stages (e.g. available resources and skills, problem formulation).
For example, where the problem demands a supervised learning algorithm, instead of an unsupervised learning algorithm, to help develop a model that can predict likely values for future instances not contained within the original dataset.

## Some Common Model Types


## Interpretability

While accuracy or predictive power may be typical goals that motivate the selection of specific model types, there are also additional factors that can influence decision-making.
One notable factor is the inherent interpretability of the model.

```{figure} /images/graphics/interpretability.png
---
align: center
name: interpretability
alt: A schematic showing the trade-off between model interpretability and model performance
---
A schematic showing the trade-off between model interpretability and model performance. Reprinted from {cite}`diop2019` 
```

## Splitting the Dataset

<!-- https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6 -->

Prior to training the model, the dataset will need to be split into 'training' and 'testing' sets to avoid model overfitting.[^overfitting^]
The *training set* is used to fit the ML model, whereas the *testing set* is a hold-out sample that is used to evaluate the fit of the ML model to the underlying data distribution. There are various methods for splitting a dataset into these components, which are widely available in popular package libraries (e.g. the scikit-learn library for the Python programming language). Again, human decision-making at this stage about the training-testing split and about how this shapes desiderata for external validation—a subsequent process where the model is validated in wholly new environments—can be very consequential for the trustworthiness and reasonableness of the development phase of an ML/AI system.

[^overfitting]: In short, overfitting occurs when a model is fit too closely to a specific set of data, likely leading to unnecessary complexity (e.g., too many features or parameters when compared to the number of observations). The model may perform very well on the training data, but perform poorly when presented with new observations.
