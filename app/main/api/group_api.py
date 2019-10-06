from flask_restplus import Namespace, fields
from app.main.exceptions import (
    ExGroupAlreadyExists
)


class GroupApi:
    api = Namespace('group', description='Inventory groups')
    dto = api.model('group', {
        'name': fields.String(required=True, description='group name'),
        'vars': fields.List(fields.Nested(api.model('vars', {
            'name': fields.String,
            'value': fields.String,
        }))),
        'namespace': fields.String(
            required=True, description='namespace', default='default'
        ),
        'children_groups': fields.List(fields.String)
    })

    @api.errorhandler(ExGroupAlreadyExists)
    def handle_group_already_exists(e):
        return {'message': 'Group already exists'}, 400
