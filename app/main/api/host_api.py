from flask_restplus import Namespace, fields
from app.main.exceptions import (
    ExNamespaceNotFound,
    ExGroupNotFound,
    ExHostAlreadyExists,
    ExHostNotFound
)


class HostApi:
    api = Namespace('host', description='Inventory hosts')
    dto = api.model('host', {
        'name': fields.String(required=True, description='host name'),
        'vars': fields.List(fields.Nested(api.model('vars', {
            'name': fields.String,
            'value': fields.String,
        }))),
        'groups': fields.List(fields.String),
        'namespace': fields.String(
            required=True, description='namespace', default='default'
        ),
    })

    @api.errorhandler(ExNamespaceNotFound)
    def handle_namespace_not_found(e):
        return {'message': 'Namespace not found'}, 400

    @api.errorhandler(ExGroupNotFound)
    def handle_group_not_found(e):
        return {'message': 'Group not found'}, 400

    @api.errorhandler(ExHostAlreadyExists)
    def handle_host_already_exists(e):
        return {'message': 'Host already exists'}, 400

    @api.errorhandler(ExHostNotFound)
    def handle_host_not_found(e):
        return {'message': 'Host not found'}, 400
