from api_config import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    funko_id = db.Column(db.Integer, db.ForeignKey("funko.id"))
    funko = db.relationship("Funko")
