from flask import Blueprint , render_template,redirect,url_for,session,request
from models.challenge import Challenge
from models.user import User
from models.course import Course
from extensions import db
from datetime import date
from models.submission import Submission

challenge_bp = Blueprint("challenge",__name__)

@challenge_bp.route("/")
def home():
    if session.get("user_id"):
        return redirect(url_for("challenge.dashboard"))
    today = date.today()
    challenges = Challenge.query.filter_by(date=today).all()
    return render_template("home.html", challenges=challenges)

@challenge_bp.route("/dashboard")
def dashboard():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))
    user = User.query.get(user_id)
    today = date.today()
    recent_challenges = Challenge.query.filter(Challenge.date <= today).order_by(Challenge.date.desc()).limit(5).all()
    categories = Course.query.all()  # Assuming Course is category
    return render_template("dashboard.html", user=user, recent_challenges=recent_challenges, categories=categories)

@challenge_bp.route("/workspace/<int:challenge_id>")
def workspace(challenge_id):
    challenge = Challenge.query.get_or_404(challenge_id)
    return render_template("workspace.html", challenge=challenge)

@challenge_bp.route("/submit/<int:challenge_id>", methods=["POST"])
def submit(challenge_id):
            user_id =session.get("user_id")
            if not user_id:
                   return redirect(url_for("auth.login"))
            
            answer = request.form["answer"]
            submission = Submission(user_id=user_id,challenge_id=challenge_id,answer=answer)

            user = User.query.get(user_id)
            user.update_streak()
            db.session.commit()
            return redirect(url_for("profile.profile"))