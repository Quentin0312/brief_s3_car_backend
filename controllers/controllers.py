import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer as mlb, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score


class tests:
    def testSKLearn():
        X = [[0, 0, 1], [2, 2, 3]]
        y = [0.5, 2.5]
        regr = svm.SVR()
        regr.fit(X, y)

        result = regr.predict([[1, 1, 3]])

        return result

    def mini_poc_test():
        # Import
        df = pd.read_csv("./datacsv/mini_poc.csv")

        # Encodage
        col = df["Manufacturer"]
        enc = OneHotEncoder()
        enc.fit(col.values.reshape(-1, 1))
        encoded_col = enc.transform(col.values.reshape(-1, 1))
        encoded_df = pd.DataFrame(encoded_col.toarray(), columns=enc.categories_[0])
        df_encoded = pd.concat([df, encoded_df], axis=1)
        df_encoded.drop(columns=["Manufacturer"], inplace=True)

        print(df_encoded.head())

        X = df_encoded.drop("Price", axis=1)
        y = df_encoded["Price"]

        print(X.head())
        print(y.head())

        # Diviser les données en ensembles de formation et de test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = svm.SVR(kernel="rbf")

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        rmse = mean_squared_error(y_test, y_pred, squared=False)
        rscore = r2_score(y_test, y_pred)
        return {"rmse": rmse, "rscore": rscore}


class estimate:
    def estimate():
        return "TODO"
