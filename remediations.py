# /python.jwt.security.unverified-jwt-decode.unverified-jwt-decode.json
import jwt
token = 'your_jwt_token'
decoded_token = jwt.decode(token, verify=False)

# /python.lang.security.audit.subprocess-shell-true.subprocess-shell-true.json
import subprocess
subprocess.call('command', shell=True)


# /python.lang.security.deserialization.avoid-pyyaml-load.avoid-pyyaml-load.json
import yaml
data = yaml.unsafe_load("payload")  # Triggers the rule


# /python.lang.security.unverified-ssl-context.unverified-ssl-context.json
import ssl
context = ssl._create_unverified_context()  # Triggers the rule


# /python.pyramid.security.sqlalchemy-sql-injection.pyramid-sqlalchemy-sql-injection.json
from pyramid.view import view_config

@view_config(...)
def example_view(request):
    query = request.dbsession.query(...)
    query.filter("user_input")  # Triggers the rule


# /python.requests.security.disabled-cert-validation.disabled-cert-validation.json
import requests
response = requests.get('https://example.com', verify=False)  # Triggers the rule


# /python.requests.security.no-auth-over-http.no-auth-over-http.json
import requests
response = requests.get('http://example.com', auth=('username', 'password'))  # Triggers the rule
