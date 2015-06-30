from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
db = SQLAlchemy(app)

from api import views, models
from reg_auth.views import reg_page

app.register_blueprint(reg_page)