from flask import Flask
from flask_cors import CORS
import config
from pack.view import view
from pack.auth import auth
from utils import db
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(view)

migrate = Migrate(app,db)
CORS(app)


if __name__ == '__main__':
    app.run()
