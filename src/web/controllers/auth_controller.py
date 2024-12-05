from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from src.web.forms.auth_form import Auth_Form
from src.core import auth
import os, binascii, jwt


bp = Blueprint("auth", __name__, url_prefix= "/auth")

@bp.get("/")
def login():
    """
    Renderiza la página de inicio de sesión con el formulario de autenticación.

    Retorna:
        render_template: Devuelve el template 'login.html' con el formulario de autenticación.
    """
    formulario = Auth_Form()
    return render_template("auth/login.html", formulario=formulario)

@bp.post("/authenticate")
def authenticate():
    """
    Autentica al usuario verificando sus credenciales y estado de bloqueo.

    Retorna:
        redirect/render_template: 
            - Redirige al formulario de login si las credenciales son incorrectas o si el usuario está bloqueado.
            - Renderiza el layout principal si la autenticación es exitosa.
    """
    params = request.form
    user = auth.check_user(params["email"], params["password"])
    if not user:
        flash("Usuario o contraseña incorrecta", "danger")
        return redirect(url_for("auth.login"))
    user = auth.check_block(user)
    if not user:
        flash("Tu usuario se encuentra bloqueado", "danger")
        return redirect(url_for("auth.login"))
    session["user"] = user.email
    flash("¡Se inició sesión correctamente!", "success")
    return render_template("layout.html")

@bp.get("/logout")
def logout():
    """
    Cierra la sesión actual del usuario, si existe, y redirige a la página de inicio de sesión.

    Retorna:
        redirect: Redirige al formulario de login, mostrando un mensaje flash dependiendo del estado de la sesión.
    """
    if session.get("user"):
        del session["user"]
        session.clear()
        flash("La sesión se cerró correctamente", "info")
    else:
        flash("No hay sesión activa", "danger")

    return redirect(url_for("auth.login"))

   
