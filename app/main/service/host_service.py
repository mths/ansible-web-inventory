from app.main import db
from app.main.model.host import Host
from app.main.model.namespace import Namespace
from app.main.service.group_service import GroupService
from app.main.service.host_variable_service import HostVariableService
from app.main.service.group_host_service import GroupHostService
from app.main.service.namespace_service import NamespaceService
from app.main.exceptions import (
    ExHostAlreadyExists,
    ExHostNotFound
)


class HostService:

    @staticmethod
    def create(data):
        host = db.session.query(Host).join(Namespace).filter(
            Namespace.name == data['namespace']
        ).filter(
            Host.name == data['name']
        ).first()

        if not host:
            try:
                namespace = NamespaceService.get_by_name(data['namespace'])

                new_host = Host(
                    name=data['name'],
                    namespace_id=namespace.id
                )

                db.session.add(new_host)
                db.session.flush()

                if 'vars' in data:
                    HostVariableService.save(data['vars'], new_host.id)

                if 'groups' in data:
                    GroupHostService.save(
                        data['groups'], new_host.id, data['namespace']
                    )

                db.session.commit()
                return new_host
            except Exception:
                raise
        else:
            raise ExHostAlreadyExists

    @staticmethod
    def update(data):
        query = db.session.query(Host).join(Namespace).filter(
            Namespace.name == data['namespace']
        ).filter(
            Host.name == data['name']
        )
        host = query.first()

        if host:
            try:
                group = GroupService.get_by_name(
                    data['namespace'], data['group']
                )
                Host.query.filter_by(id=host.id).update({'group_id': group.id})

                if 'vars' in data:
                    HostVariableService.save(data['vars'], query.first().id)

                db.session.commit()
                return query.first()
            except Exception:
                raise
        else:
            raise ExHostNotFound

    @staticmethod
    def delete(namespace: str, host: str):
        query = db.session.query(Host).join(Namespace).filter(
            Namespace.name == namespace
        ).filter(
            Host.name == host
        )
        host = query.first()

        if host:
            try:
                db.session.delete(host)
                db.session.commit()
                return True
            except Exception:
                raise
        else:
            raise ExHostNotFound

    @staticmethod
    def get_all_from_namespace(namespace: str):
        return db.session.query(Host).join(Namespace).filter(
            Namespace.name == namespace
        ).all()
