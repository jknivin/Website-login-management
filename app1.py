from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    logs = db.relationship("Log", backref="user", lazy=True)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    logout_time = db.Column(db.DateTime)

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            log = Log(user_id=user.id)
            db.session.add(log)
            db.session.commit()
            return redirect(url_for("profile"))
        flash("Invalid email or password")
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.email.data == "admin@example.com":
            flash("This email is reserved. Please use a different email.")
            return render_template("register.html", form=form)
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/profile")
@login_required
def profile():
    if current_user.is_admin:
        users = User.query.all()
        logs = Log.query.all()
        return render_template("admin_profile.html", users=users, logs=logs)
    return render_template("user_profile.html")

@app.route("/logout")
@login_required
def logout():
    log = Log.query.filter_by(user_id=current_user.id, logout_time=None).first()
    if log:
        log.logout_time = datetime.utcnow()
        db.session.commit()
    logout_user()
    return redirect(url_for("home"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(email="admin@example.com").first()
        if not admin:
            hashed_password = generate_password_hash("admin")
            admin = User(email="admin@example.com", password=hashed_password, is_admin=True)
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)
