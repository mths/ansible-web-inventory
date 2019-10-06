from flask_restplus import Api
from flask import Blueprint
from app.main.controller.host import api as host_ns
from app.main.controller.group import api as group_ns


blueprint = Blueprint('api', __name__)

api = Api(
          title='Ansible web inventory',
          version='1.0',
          description='Web inventory service for maintaining awi'
          )

api.init_app(blueprint)
api.add_namespace(host_ns)
api.add_namespace(group_ns)
