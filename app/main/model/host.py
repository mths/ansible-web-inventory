from app.main import db
from sqlalchemy.orm import relationship
from app.main.model.host_variable import HostVariable
from app.main.model.namespace import Namespace


class Host(db.Model):
    """ Host Model for storing inventory hosts """
    __tablename__ = "host"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    namespace_id = db.Column(db.Integer, db.ForeignKey('namespace.id'))
    vars = relationship(
        HostVariable, back_populates="host", cascade="delete"
    )

    namespace = relationship(Namespace, back_populates="hosts")
    groups = relationship("GroupHost", back_populates="host", cascade="delete")
