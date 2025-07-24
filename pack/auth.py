from flask import Blueprint, request, jsonify, session
from models import UserModel

auth = Blueprint("auth",__name__,url_prefix="/auth")

@auth.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    id = data.get("id")
    password = data.get("password")
    print(id,password,request.data)
    user = UserModel.query.filter_by(id=id,password=password).first()
    if not user:
        return jsonify({"success":False})
    else:
        session["id"] = user.id
        session["username"] = user.username
        # session["token"] = user.token
        return jsonify({"success":True,"username":user.username})

# @auth.route("/register",methods=["GET","POST"])
# def register():
#     if request.method == "GET":
#         return render_template("register.html")
#     else:
#         username = request.form.get("username")
#         password = request.form.get("password")
#         user = UserModel(username=username,password=password)
#         db.session.add(user)
#         db.session.commit()
#         return "ok"



