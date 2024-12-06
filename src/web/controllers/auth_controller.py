from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from src.web.forms.auth_form import Auth_Form
from src.core.models import auth
from src.web.handlers.auth import check_auth
import os, binascii, jwt


bp = Blueprint("auth", __name__, url_prefix= "/auth")

@bp.get("/")
@check_auth()
def login():
    """
    Renderiza la página de inicio de sesión con el formulario de autenticación.

    Retorna:
        render_template: Devuelve el template 'login.html' con el formulario de autenticación.
    """
    formulario = Auth_Form()
    return render_template("auth/login.html", formulario=formulario)

@bp.post("/authenticate")
@check_auth()
def authenticate():
    """
    Autentica al usuario verificando sus credenciales

    Retorna:
        redirect/render_template: 
            - Redirige al formulario de login si las credenciales son incorrectas o si el usuario está bloqueado.
            - Renderiza el layout principal si la autenticación es exitosa.
    """
    params = request.form
    user = auth.check_user(params["email"], params["contraseña"])
    if not user:
        flash("Usuario o contraseña incorrecta", "danger")
        return redirect(url_for("auth.login"))
    session["user_email"] = user.email
    session["user_name"] = user.nombre
    session["user_id"] = user.id
    flash("¡Se inició sesión correctamente!", "success")
    return redirect(url_for("home"))

@bp.get("/logout")
def logout():
    """
    Cierra la sesión actual del usuario, si existe, y redirige a la página de inicio de sesión.

    Retorna:
        redirect: Redirige al formulario de login, mostrando un mensaje flash dependiendo del estado de la sesión.
    """
    if session.get("user_email"):
        del session["user_email"]
        del session["user_name"]
        del session["user_id"]
        session.clear()
        flash("La sesión se cerró correctamente", "info")

    return redirect(url_for("auth.login"))

   
