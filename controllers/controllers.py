import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split



class tests:
    def testSKLearn():
        X = [[0, 0, 1], [2, 2, 3]]
        y = [0.5, 2.5]
        regr = svm.SVR()
        regr.fit(X, y)

        result = regr.predict([[1, 1, 3]])
        
        return result