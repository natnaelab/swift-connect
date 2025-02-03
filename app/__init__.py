import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "%ze$$1sb2A8#*p3wtqtx7ab%OBwBU1Z0$R44ro"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"  -- for quick testing
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@localhost/swift_connect".format(
    os.getenv("DB_USER"), os.getenv("DB_PASSWORD")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app import routes
