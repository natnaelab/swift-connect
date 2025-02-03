from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, OnboardingRequest
from app.forms import LoginForm, OnboardingForm


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid username or password")
    return render_template("login.html", form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "business":
        requests = OnboardingRequest.query.filter_by(user_id=current_user.id).all()
    else:
        requests = OnboardingRequest.query.filter_by(status="submitted").all()
    return render_template("dashboard.html", requests=requests)


@app.route("/onboarding", methods=["GET", "POST"])
@login_required
def onboarding():
    form = OnboardingForm()
    if form.validate_on_submit():
        request = OnboardingRequest(
            user_id=current_user.id,
            company_name=form.company_name.data,
            swift_code=form.swift_code.data,
            status="submitted",
        )
        db.session.add(request)
        db.session.commit()
        flash("Request submitted successfully")
        return redirect(url_for("dashboard"))
    return render_template("onboarding.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/request/<int:request_id>/<action>")
@login_required
def handle_request(request_id, action):
    if current_user.role == "business":
        flash("Not authorized")
        return redirect(url_for("dashboard"))

    request = OnboardingRequest.query.get_or_404(request_id)
    if action == "approve":
        request.status = "approved"
        flash("Request approved")
    elif action == "reject":
        request.status = "rejected"
        flash("Request rejected")

    db.session.commit()
    return redirect(url_for("dashboard"))
