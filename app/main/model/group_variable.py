from app.main import db
from sqlalchemy.orm import relationship


class GroupVariable(db.Model):
    """ GroupVariable Model for storing inventory Groups variables """
    __tablename__ = "group_variable"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    value = db.Column(db.String(1024), unique=False, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = relationship("Group", back_populates="vars")
