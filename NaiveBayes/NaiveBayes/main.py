#%%
from NaiveBayes import *


targetAttribute = 'targetattr'

attributes = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'targetattr']

features = attributes.copy()
features.remove(targetAttribute)

# dataset = pd.read_csv('cse353-hw2-data.tsv', sep='\t', names=attributes)

def generateRange(start, end, breakpoints):
    return list(zip([start] + breakpoints, breakpoints + [end]))

def check(naiveBayesFunc, testset):
    count = 0
    for i in testset.index:
        if naiveBayesFunc(testset.ix[i]) == testset.ix[i][targetAttribute]:
            count+=1
    return count/np.size(testset, axis=0)

def nFoldCheck(data, n):
    ranges = generateRange(0, len(data), [len(data)*i//n for i in range(1, n+1)][:-1])
    result = []
    for i, j in ranges:
        trainset = pd.concat([data.iloc[:i], data.iloc[j:]])
        f = naiveBayes(trainset, features, targetAttribute)
        testset = data.iloc[i:j]
        result.append(check(f, testset))
    return (result, sum(result)/n)

# print(nFoldCheck(dataset[:1000],5))

import os
print(os.getcwd())