from flask import Blueprint,render_template ,session
from models.user import User

profile_bp = Blueprint("profile",__name__)

@profile_bp.route("/profile")
def profile():
    user = User.query.get(session.get("user_id"))
    return render_template("profile.html", user=user)