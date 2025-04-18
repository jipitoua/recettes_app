from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Identifiants incorrects")
    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User(email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
