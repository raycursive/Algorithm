import numpy as np
import pandas as pd
from scipy.stats import norm


def isContinuous(dataset, attribute):
    return dataset[attribute].dtype in ['int64', 'float64']

class logLikelihood():
    def __init__(self, dataset, grandTotal, attribute, targetAttribute):
        self.targetAttribute = targetAttribute
        self.isContinuous = isContinuous(dataset, attribute)
        self.attribute = attribute
        self.attributeValues = dataset[attribute].unique()
        self.laplacian = (grandTotal+len(self.attributeValues))
        if isContinuous(dataset, attribute):
            table = pd.DataFrame(dataset,columns=[attribute,targetAttribute])
            self.gaussian = dict()
            for target in dataset[targetAttribute].unique():
                mean = table[table[targetAttribute] == target].mean()
                var = table[table[targetAttribute] == target].var()
                self.gaussian[target] = norm(mean, np.sqrt(var))
        else:
            #self.table = dataset.groupby([attribute, targetAttribute]).size() / grandTotal
            self.table = (dataset.groupby([attribute, targetAttribute]).size()+1) / self.laplacian     # Laplacian correction
            self.table = np.log(self.table)

    def value(self, attributeValue, target):
        if self.isContinuous:
            return self.gaussian[target].logpdf(attributeValue)
        else:
            if attributeValue in self.attributeValues and target in self.table[attributeValue]:
                    return self.table[attributeValue][target]
            return np.log(1/self.laplacian[target])


def predict(instance, features, loglikelihoodTable, prior, targetAttrs):
    pred = dict()
    for target in targetAttrs:
        pred[target] = prior[target]
        for attr in features:
            pred[target] += loglikelihoodTable[attr].value(instance[attr], target)
    return max(pred, key = lambda x: pred[x])


def naiveBayes(trainset, features, targetAttribute):
    num_samples = np.size(trainset, axis=0)
    targetAttrs = trainset[targetAttribute].unique()
    grandTotal = trainset.groupby(targetAttribute).size()
    prior = grandTotal / num_samples
    #prior = np.log((grandTotal+1) / (num_samples+len(targetAttrs)))
    loglikelihoodTable = {attr:logLikelihood(trainset, grandTotal, attr, targetAttribute) for attr in features}
    return lambda i: predict(i, features, loglikelihoodTable, prior, targetAttrs)


