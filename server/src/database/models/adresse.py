from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

db = SQLAlchemy()

class Adresse(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    region = db.Column(db.String(80), nullable=False)
    adresse = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)