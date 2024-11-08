from flask import Blueprint, render_template

auth_db = Blueprint('auth', __name__, url_prefix="/auth")

@auth_db.route("/")
def auth():
    return render_template('auth.html')

