from flask import render_template
from flask import Blueprint
from api import app

reg_page = Blueprint('register', __name__, template_folder='templates')


@app.route('/')
def register():
    return render_template('register.html')