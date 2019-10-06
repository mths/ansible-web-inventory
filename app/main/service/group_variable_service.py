from app.main import db
from app.main.model.group_variable import GroupVariable
from app.main.exceptions import ExCouldNotDeleteGroupVariable


class GroupVariableService:
    @staticmethod
    def save(variables: dict, group_id: int):
        GroupVariableService.delete_by_group(group_id)

        for variable in variables:
            db.session.add(GroupVariable(
                name=variable['name'],
                value=variable['value'],
                group_id=group_id
            ))

    @staticmethod
    def delete_by_group(group_id: int):
        try:
            GroupVariable.query.filter_by(group_id=group_id).delete()
        except Exception:
            raise ExCouldNotDeleteGroupVariable

    @staticmethod
    def get_all(group_id: int):
        return GroupVariable.query.filter_by(group_id=group_id).all()
