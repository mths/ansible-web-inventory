from app.main import db
from sqlalchemy.orm import relationship


class Namespace(db.Model):
    """ Namespace model for storing namespaces"""
    __tablename__ = "namespace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    hosts = relationship("Host", back_populates="namespace")

    def __repr__(self):
        return str(self.name)
