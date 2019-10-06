from flask_restplus import Resource
from flask import request
from app.main.api.group_api import GroupApi
from app.main.service.group_service import GroupService

api = GroupApi.api
dto = GroupApi.dto


@api.route('/<namespace>')
class GroupList(Resource):
    @api.doc('List groups from inventory namespace')
    @api.marshal_list_with(dto)
    @api.doc(params={'namespace': 'Namespace name'})
    def get(self, namespace):
        """List all group from inventory namespace"""
        return GroupService.get_all_from_namespace(namespace)


@api.route('/')
class Group(Resource):

    @api.expect(dto, validate=True)
    @api.response(201, 'Group successfully created.')
    @api.doc('create a new group')
    def post(self):
        """Creates a new group """
        try:
            data = request.json
            GroupService.create(data=data)
            return {'message': 'Group successfully created.'}, 201
        except Exception:
            raise

    @api.expect(dto, validate=True)
    @api.response(201, 'Group successfully updated.')
    @api.doc('update a group')
    def put(self):
        """Updates a group """
        try:
            data = request.json
            GroupService.update(data=data)
            return {'message': 'Group successfully update.'}, 201
        except Exception:
            raise


@api.route('/<namespace>/<group>')
class GroupDelete(Resource):
    @api.response(201, 'Group successfully updated.')
    @api.doc('update a group')
    def delete(self, namespace, group):
        """Deletes a group """
        try:
            GroupService.delete(namespace, group)
            return {'message': 'Group successfully deleted.'}, 201
        except Exception:
            raise
