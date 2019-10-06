from app.main import db
from sqlalchemy.orm import relationship


class GroupHost(db.Model):
    """ GroupVariable Model for storing inventory Groups hosts """
    __tablename__ = "group_host"

    group_id = db.Column(
        db.Integer, db.ForeignKey('group.id'), primary_key=True,
    )
    host_id = db.Column(
        db.Integer, db.ForeignKey('host.id'), primary_key=True,
    )
    host = relationship("Host", back_populates="groups")
    group = relationship("Group", back_populates="hosts")

    def __repr__(self):
        return str(self.group.name)
