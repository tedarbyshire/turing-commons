# Model Testing and Validation

<!--  
Test
A test uses pass / fail criteria to check a specific, single function.

Evaluation
An evaluation combines multiple tests and experimental use, to provide an overall judgement.

Verification
Verification is the act of checking against a specification. It asks, ‘did we build the thing right?’ or ‘are we doing the thing right?’

Tests are usually associated with verification.

Validation
Validation is the act of checking against an end user’s need. It asks, ‘did we build the right thing?’ or ‘are we doing the right thing?’
-->

[DSTL Biscuit Book](https://www.gov.uk/government/publications/assurance-of-ai-and-autonomous-systems-a-dstl-biscuit-book/assurance-of-artificial-intelligence-and-autonomous-systems-a-dstl-biscuit-book)

The testing set is typically kept separate from the training set, in order to provide an unbiased evaluation of the final model fit on the training dataset. However, the training set can be further split to create a validation set, which can then be used to evaluate the model while also *tuning model hyperparameters*. This process can be performed repeatedly, in a technique known as (k-fold) cross-validation, where the training data are resampled (*k*-times) to compare models and estimate their performance in general when used to make predictions on unseen data. This type of validation is also known as 'internal validation', to distinguish it from external validation, and, in a similar way to choices made about the training-testing split, the manner in which it is approached can have critical consequences for how the performance of a system is measured against the real-world conditions that it will face when operating “in the wild.”