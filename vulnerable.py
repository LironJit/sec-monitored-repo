# /python.pyramid.security.sqlalchemy-sql-injection.pyramid-sqlalchemy-sql-injection.json
from pyramid.view import view_config
from sqlalchemy import func
from myapp.models import MyModel


@view_config(route_name='example', renderer='json')
def example_view(request):
    user_input = request.params.get('user_input')

    query = request.dbsession.query(MyModel)
    query = query.filter("column_name = '{}'".format(user_input))

    results = query.all()

    return {'results': results}


# /python.lang.security.deserialization.avoid-pyyaml-load.avoid-pyyaml-load.json
import yaml
data = yaml.unsafe_load("payload")  # Triggers the rule

# /python.lang.security.unverified-ssl-context.unverified-ssl-context.json
import ssl
context = ssl._create_unverified_context()  # Triggers the rule
