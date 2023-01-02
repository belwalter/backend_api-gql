
from api_config import db

class Funko(db.Model):
    __tablename__ = "funko"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String(50))
    collection = db.Column(db.String(70))
