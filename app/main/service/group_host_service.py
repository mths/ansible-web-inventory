from app.main import db
from app.main.model.group_host import GroupHost
from app.main.service.group_service import GroupService
from app.main.exceptions import ExCouldNotDeleteGroupHost


class GroupHostService:
    @staticmethod
    def save(groups: list, host_id: int, namespace: str):
        GroupHostService.delete_by_host(host_id)

        for addgroup in groups:
            group = GroupService.get_by_name(namespace, addgroup)

            db.session.add(GroupHost(
                host_id=host_id,
                group_id=group.id
            ))

    @staticmethod
    def delete_by_host(host_id: int):
        try:
            GroupHost.query.filter_by(host_id=host_id).delete()
        except Exception:
            raise ExCouldNotDeleteGroupHost
