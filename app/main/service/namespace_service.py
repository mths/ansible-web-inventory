from app.main.model.namespace import Namespace
from app.main.exceptions import ExNamespaceNotFound


class NamespaceService:
    @staticmethod
    def get_by_name(name: str):
        namespace = Namespace.query.filter_by(name=name).first()
        if not namespace:
            raise ExNamespaceNotFound
        else:
            return namespace
