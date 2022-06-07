from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from main import db
class User(db.Model):

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = db.Column(db.String(255), unique=True, nullable=False,index=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False,index=True)
    phone_number = db.Column(db.String(8), unique=True, nullable=False)
    sexe = db.Column(db.String(1), nullable=True)
    adresse_id = db.Column(UUID(as_uuid=True), ForeignKey('adresse.id'))

