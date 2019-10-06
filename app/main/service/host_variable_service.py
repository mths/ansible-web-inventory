from app.main import db
from app.main.model.host_variable import HostVariable
from app.main.exceptions import ExCouldNotDeleteHostVariable


class HostVariableService:
    @staticmethod
    def save(variables: dict, host_id: int):
        HostVariableService.delete_by_host(host_id)

        for variable in variables:
            db.session.add(HostVariable(
                name=variable['name'],
                value=variable['value'],
                host_id=host_id
            ))

    @staticmethod
    def delete_by_host(host_id: int):
        try:
            HostVariable.query.filter_by(host_id=host_id).delete()
        except Exception:
            raise ExCouldNotDeleteHostVariable

    @staticmethod
    def get_all(host_id: int):
        return HostVariable.query.filter_by(host_id=host_id).all()
