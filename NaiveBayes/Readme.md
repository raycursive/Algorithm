A implementation of Naive Bayes Classifier by Python 3
-----------------------

Environment:    Python 3
Dependency:     numpy for vectorization and math operations
                pandas for data structure (DataFrame)
                scipy.stats for the object of normal distribution

-----------------------

## Introduction

The algorithm of naive Bayes is in `NaiveBayes.py`, and `main.py` is for data preprocessing and generate the result of 5-fold cross validation.

The main part of naive Bayes classifier is the likelihood table, which is defined as a class `logLikelihood`. The reason why all values has been applied a logrithm function is to avoid underflow, and change all multiplications to additions in calculating the proportion of posterior probability.

In the initialization of `logLikelihood`, for discrete-valued attribute, we calculated its likelihood table, and for continuous-valued attribute, we calculated its probabilistic distribution. For discrete-valued case, to handle missing attribute values, we introduced laplacian smoothness to avoid zero probability.

The `predict` function is to use all information we need to predict the target attribute for a instance, which is basically an argmax for all target attribute values.

The `naiveBayes` function is like a boxing of all things above, simply accept least parameters and return a function which accept a instance and return a prediction.

-----------------------
## How to use it

To check the accuracy, just run `nFoldCheck(dataset, 5)` and wait. It's a little bit slow.
