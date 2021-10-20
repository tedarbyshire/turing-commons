# Model Selection and Training

- Selecting models for interpretability
- The limitations of technical tools for fairness
- Model generalisability

This stage determines the model type and structure that will be produced in the next stages. In some projects, model selection will result in multiple models for the purpose of comparison based on some performance metric (e.g. accuracy). In other projects, there may be a need to first of all implement a pre-existing set of formal models into code. The class of relevant models is likely to have been highly constrained by many of the previous stages (e.g. available resources and skills, problem formulation), for instance, where the problem demands a supervised learning algorithm instead of an unsupervised learning algorithm; or where explainability considerations require a more interpretable model (e.g. a decision tree).

Prior to training the model, the dataset will need to be split into training and testing sets to avoid model overfitting. The *training set* is used to fit the ML model, whereas the *testing set* is a hold-out sample that is used to evaluate the fit of the ML model to the underlying data distribution. There are various methods for splitting a dataset into these components, which are widely available in popular package libraries (e.g. the scikit-learn library for the Python programming language). Again, human decision-making at this stage about the training-testing split and about how this shapes desiderata for external validation—a subsequent process where the model is validated in wholly new environments—can be very consequential for the trustworthiness and reasonableness of the development phase of an ML/AI system.
