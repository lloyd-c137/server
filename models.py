from utils import db
import uuid

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    token = db.Column(db.String(255),default=uuid.uuid4())
    mbti= db.Column(db.String(255),nullable=True)
    like = db.Column(db.String(255),nullable=True)
    interepoint = db.Column(db.String(255),nullable=True)
    output = db.Column(db.String(255),nullable=True)
    tags = db.Column(db.String(255),nullable=True)
