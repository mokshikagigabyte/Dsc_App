from flask import Blueprint , render_template , request , redirect, url_for, session,flash
from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash("Login Successful!", "success")
            return redirect(url_for("challenge.home"))
        else:
            flash("Invalid email or password", "danger")
    return render_template("login.html")
    
@auth_bp.route("/signup", methods=["GET","POST"])
def signup():
   if request.method == "POST":
       email = request.form["email"]
       password = generate_password_hash( request.form["password"])
     
       existing_user = User.query.filter_by(email=email).first()
       if existing_user:
           flash("Email already registered. Please login instead.", "danger")
           return redirect(url_for("auth.login"))
       
       user = User(email=email,password=password)
       db.session.add(user)
       db.session.commit()
       flash("Signup successful! Please login.","success")
       return redirect(url_for("auth.login")) 
   return render_template("signup.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("auth.login"))