from app.main import db
from sqlalchemy.orm import relationship


class HostVariable(db.Model):
    """ HostVariable Model for storing inventory hosts variables """
    __tablename__ = "host_variable"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    value = db.Column(db.String(1024), unique=False, nullable=False)
    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))
    host = relationship("Host", back_populates="vars")
