import requests
from flask import Blueprint,jsonify,request
from models import UserModel,TasksModel
from utils import db
import json
from datetime import datetime

def timeNow():
    return datetime.now().strftime("%Y-%m-%d")
view = Blueprint("view",__name__,url_prefix="/api/users")

@view.route("/")
def index():
    return "index"

# 获取用户画像
@view.route("/<int:userid>/profile")
def profile(userid):
    user = UserModel.query.filter_by(id=userid).first()
    return jsonify({
        "code":0,
        "data":{
            "userId":userid,
            "mbti":user.mbti,
            "tags":user.tags,
            "behavior_weights":user.behavior_weights
        }
    })

# 提交任务或习惯目标
@view.route("/<int:userid>/tasks",methods=["POST"])
def tasks(userid):
    data = request.get_json()
    title = data.get("title")
    type = data.get("type")
    way = data.get("way")
    # duration = data.get("duration")
    detail = {
        "title":title,
        "type":type,
        "way":way
        # "duration":duration
    }
    detail = json.dumps(detail)
    task = TasksModel(userid=userid,detail=detail)
    db.session.add(task)
    db.session.commit()
    return jsonify({"code":0,"message":"任务添加成功"})

# 获取当天所有任务及状态
@view.route("/<int:userid>/tasks/today")
def today(userid):
    tiMe = timeNow
    task = TasksModel.query.filter_by(start_time=tiMe).all()
    return jsonify({"code":0,"data":{"taskid":[task.id,task.detail]},"status": task.status})


# 用户偏好排序与权重更新
@view.route("/<int:userid>/preferences/order",methods=["POST"])
def preorder(userid):
    user = UserModel.query.filter_by(id=userid).first()
    data = request.get_json()
    orderedPreferences = data.get("orderedPreference")
    # requests.post(orderedPreferences)
    return jsonify({"code":0,"message":"权重更新成功","data":user.behavior_weights})

# 标记任务完成
@view.route("/<int:userid>/tasks/complete",methods=["POST"])
def taks_complete(userid):
    taskid = request.get_json()["taskid"]
    task = TasksModel.query.filter_by(id=taskid).first()
    task.status = "complete"
    return jsonify({ "code": 0, "message": "标记完成成功" })

@view.route("/<int:userid>/recommendations?limit=<int:n>",methods=["POST"])
def get_commend():
    pass

# 设置/获取休息偏好
@view.route("/<int:userid>/rest/preferences",methods=["GET","POST"])
def rest_preferences(userid):
    if request.method == "GET":
        return jsonify({"level":1,"preferredDuration":[1,1]})
    else:
        level = request.json.get("level")
        preferredDuration = request.json.get("preferredDuration")
        return jsonify({"code":0,"message":"偏好设置成功"})

@view.route("/<int:userid>/habits/<int:habitid>/log",methods=["POST"])
def habit_log(userid,habitid):

    return jsonify({"code":0,"message":"打卡成功"})