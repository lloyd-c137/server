from sqlalchemy import ForeignKey

from utils import db
from datetime import datetime

def timeNow():
    return datetime.now().strftime("%Y-%m-%d")
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    mbti= db.Column(db.String(255),nullable=True)
    output = db.Column(db.String(255),nullable=True)
    #字符串
    tags = db.Column(db.String(255),nullable=True)
    behavior_weights = db.Column(db.Text,nullable=True)

class TasksModel(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    userid = db.Column(db.Integer,ForeignKey("user.id"))
    start_time = db.Column(db.String(255),default=timeNow)
    detail = db.Column(db.Text,nullable=True)
    status = db.Column(db.String(255),default="in_progress")
