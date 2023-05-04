import hug
from hug.middleware import CORSMiddleware
from controllers.controllers import tests
api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))

api_base_url = "/api"

hug.get(api_base_url + "/sklearnTest", api=api)(tests.testSKLearn)
hug.get(api_base_url + "/mini_poc_test", api=api)(tests.mini_poc_test)
