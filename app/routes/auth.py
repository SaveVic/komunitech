from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user
from app.forms.auth_form import LoginForm, RegistrationForm
from app.services.auth_service import AuthService
from app.utils.decorators import logout_required

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/")
def index():
    return redirect(url_for("auth.login"))


@auth_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        result = AuthService.register(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        success = result.get("success", False)
        user = result.get("user")
        if success:
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            message = result.get("error", "Terjadi kesalahan")
            flash(result.get("error", message), "danger")

    return render_template("auth/register.html", title="Register", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        result = AuthService.login(
            username=form.username.data, password=form.password.data
        )
        success = result.get("success", False)
        user = result.get("user")
        if success:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            message = result.get("error", "Terjadi kesalahan")
            flash(result.get("error", message), "danger")

    return render_template("auth/login.html", title="Login", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
