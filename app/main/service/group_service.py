from app.main import db
from app.main.model.group import Group
from app.main.model.namespace import Namespace
from app.main.service.namespace_service import NamespaceService
from app.main.service.group_variable_service import GroupVariableService
from app.main.exceptions import (
    ExGroupAlreadyExists,
    ExGroupNotFound
)


class GroupService:
    @staticmethod
    def create(data):
        group = db.session.query(Group).join(Namespace).filter(
            Namespace.name == data['namespace']
        ).filter(
            Group.name == data['name']
        ).first()

        if not group:
            try:
                namespace = NamespaceService.get_by_name(data['namespace'])

                new_group = Group(
                    name=data['name'],
                    namespace_id=namespace.id,
                    children_groups=','.join(data.get('children_groups', []))
                )

                db.session.add(new_group)
                db.session.flush()

                if vars in data:
                    GroupVariableService.save(data['vars'], new_group.id)

                db.session.commit()
                return new_group
            except Exception:
                raise
        else:
            raise ExGroupAlreadyExists

    @staticmethod
    def update(data):
        query = db.session.query(Group).join(Namespace).filter(
            Namespace.name == data['namespace']
        ).filter(
            Group.name == data['name']
        )
        group = query.first()

        if group:
            try:
                Group.query.filter_by(id=group.id).update({
                    'children_groups': ','.join(
                        data.get('children_groups', [])
                    )
                })

                if 'vars' in data:
                    GroupVariableService.save(data['vars'], query.first().id)

                db.session.commit()
                return query.first()
            except Exception:
                raise
        else:
            raise ExGroupNotFound

    @staticmethod
    def delete(namespace: str, group: str):
        query = db.session.query(Group).join(Namespace).filter(
            Namespace.name == namespace
        ).filter(
            Group.name == group
        )
        group = query.first()

        if group:
            try:
                return Group.query.filter_by(id=group.id).delete()
            except Exception:
                raise
        else:
            raise ExGroupNotFound

    @staticmethod
    def get_by_name(namespace: str, name: str):
        group = db.session.query(Group).join(Namespace).filter(
            Namespace.name == namespace
        ).filter(
            Group.name == name
        ).first()

        if not group:
            raise ExGroupNotFound
        else:
            return group

    @staticmethod
    def get_all_from_namespace(namespace: str):
        return db.session.query(Group).join(Namespace).filter(
            Namespace.name == namespace
        ).all()

    @staticmethod
    def save(data):
        db.session.add(data)
        db.session.commit()
