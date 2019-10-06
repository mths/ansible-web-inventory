from app.main import db
from sqlalchemy.orm import relationship
from app.main.model.group_variable import GroupVariable


class Group(db.Model):
    """ Group Model for storing inventory group """
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    _children_groups = db.Column("children_groups", db.String(255), unique=False, nullable=False)
    namespace_id = db.Column(db.Integer, db.ForeignKey('namespace.id'))
    vars = relationship(
        GroupVariable, back_populates="group", cascade="delete"
    )
    hosts = relationship("GroupHost", back_populates="group", cascade="delete")

    def __repr__(self):
        return str(self.name)

    @property
    def children_groups(self):
        return self._children_groups.split(',')

    @children_groups.setter
    def children_groups(self, children_groups):
        self._children_groups = children_groups
