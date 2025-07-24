from flask import Blueprint,jsonify
from models import UserModel
view = Blueprint("view",__name__,url_prefix="/api")

@view.route("/")
def index():
    return "index"

@view.route("users/<int:userid>/profile")
def profile(userid):
    user = UserModel.query.filter_by(id=userid).first()
    return jsonify({
        "code":0

    })
