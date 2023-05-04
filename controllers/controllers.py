import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

# Préparer les datas du csc pour l'IA => encodage, normalisation, ...


# Charger les datas du csv
# Entrainer
# Prédire


class tests:
    def testSKLearn():
        X = [[0, 0, 1], [2, 2, 3]]
        y = [0.5, 2.5]
        regr = svm.SVR()
        regr.fit(X, y)

        result = regr.predict([[1, 1, 3]])

        return result

    def mini_poc_test():
        df = pd.read_csv('./datacsv/mini_poc.csv')
        test = len(df.index)
        return test
