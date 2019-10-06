from flask_restplus import Resource
from flask import request
from app.main.api.host_api import HostApi
from app.main.service.host_service import HostService

api = HostApi.api
dto = HostApi.dto


@api.route('/<namespace>')
class HostList(Resource):
    @api.doc('List hosts from inventory namespace')
    @api.marshal_list_with(dto)
    @api.doc(params={'namespace': 'Namespace name'})
    def get(self, namespace):
        """List all hosts from inventory namespace"""
        return HostService.get_all_from_namespace(namespace)


@api.route('/')
class Host(Resource):
    @api.expect(dto, validate=True)
    @api.response(201, 'Host successfully created.')
    @api.doc('create a new host')
    def post(self):
        """Creates a new host """
        try:
            data = request.json
            HostService.create(data=data)
            return {'message': 'Host successfully created.'}, 201
        except Exception:
            raise

    @api.expect(dto, validate=True)
    @api.response(201, 'Host successfully updated.')
    @api.doc('update a host')
    def put(self):
        """Creates a new host """
        try:
            data = request.json
            HostService.update(data=data)
            return {'message': 'Host successfully update.'}, 201
        except Exception:
            raise


@api.route('/<namespace>/<host>')
class HostDelete(Resource):
    @api.response(201, 'Host successfully updated.')
    @api.doc('update a Host')
    def delete(self, namespace, host):
        """Deletes a Host """
        try:
            HostService.delete(namespace, host)
            return {'message': 'Host successfully deleted.'}, 201
        except Exception:
            raise
