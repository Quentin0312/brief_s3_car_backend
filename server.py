import hug
from hug.middleware import CORSMiddleware
from sklearn import svm
api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))


@hug.get("/sklearnTest")
def hello_world():
    X = [[0, 0], [2, 2]]
    y = [0.5, 2.5]
    regr = svm.SVR()
    regr.fit(X, y)

    result = regr.predict([[1, 1]])
    return result
