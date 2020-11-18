from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from server.config import Config

app = Flask(__name__, template_folder="../templates", static_folder="../static", static_url_path='/static')
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from server.routes import *
from server.models import *

import sqlalchemy as sa

if not sa.inspect(db.engine).get_table_names():
    db.create_all()
