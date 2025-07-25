from flask import Blueprint, request,jsonify
from datetime import datetime

api = Blueprint('api', __name__, url_prefix='/api')


# 行为推荐生成
@api.route("/recommandations/generate",methods=["POST"])
def index():
    userid = request.json.get("userid")
    datetime = request.json.get("datetime")
    daily_goal = request.json.get("daily_goal")
    preferred_type = request.json.get("preferred_type")
    context = request.json.get("context")
    return jsonify({"recommendations":[{"id":1,"title":1,"type":1,"indensity":1,"category":1}],
                    "source_weights":{
                        "user_mbti_match":1,
                        "behavoir_history":1,
                        "daily_goal_alignment":1,
                        "type_match":1,
                        "context_fit":1,
                    },
                    "updated_profile":{
                        "creative":1,
                        "outdoor":1,
                        "congnitive":1,
                        "passive":1
                    }
    })

@api.route("/agent/analyze",methods=["POST"])
def analyze():
    userid = request.json.get("userid")
    fontendInput = request.json.get("fontendInput")
    return jsonify({"summary":1,"suggestions":1})