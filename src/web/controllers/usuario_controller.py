from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from src.core.services import usuario_service
from src.web.handlers.permisos import check
from src.web.forms import Usuario_Form
from src.web.forms.recuperar_contraseña_form import RecuperarContraseñaForm

usuario_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@usuario_bp.get("/")
@check("usuarios_listar")
def listar():
    pagina = request.args.get('pagina', 1, type=int)
    roles = usuario_service.listar_roles()
    roles = [rol for rol in roles if rol.nombre != "presidencia_jefe"]
    usuarios = usuario_service.listar_usuarios(pagina)
    valores_actuales = {
        'nombre': request.args.get('nombre'),
        'email': request.args.get('email'),
        'rol': request.args.get('rol'),
        'sort': request.args.get('sort'),
        'order': request.args.get('order')
    }
    return render_template("usuarios/listar_usuarios.html", usuarios=usuarios, roles=roles, actuales=valores_actuales)

@usuario_bp.route("/crear", methods=['GET', 'POST'])
@check("usuarios_crear")
def crear_usuario():
    '''
    Crea un usuario.
    
    Returns:
        render_template: La plantilla de crear usuario.
    '''
    formulario = Usuario_Form()
    roles = usuario_service.listar_roles()
    formulario.id_rol.choices = [("", "Seleccione un rol")] + [(rol.id, rol.nombre) for rol in roles if rol.nombre != "alumno" and rol.nombre != "presidencia_jefe"]
    if formulario.validate_on_submit():
        usuario_service.crear_usuario(formulario)
        return redirect("/usuarios")
    return render_template("usuarios/crear_usuario.html", formulario=formulario)

@usuario_bp.get("detalle/<int:id_usuario>")
@check("usuarios_detalle")
def ver_detalle_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    roles = usuario_service.listar_roles()
    formulario = Usuario_Form(obj=usuario)
    formulario.id_rol.choices = [(rol.id, rol.nombre) for rol in roles]
    return render_template("usuarios/detalle_usuario.html", formulario=formulario, usuario=usuario)


@usuario_bp.route("/editar/<int:id_usuario>", methods=['POST'])
@check("usuarios_editar")   
def editar_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    formulario = Usuario_Form(obj=usuario, id_usuario_editado=id_usuario)
    return render_template("usuarios/editar_usuario.html", formulario=formulario, usuario=usuario)

@usuario_bp.route("/actualizar/<int:id_usuario>", methods=['POST'])
@check("usuarios_editar")
def actualizar_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    formulario = Usuario_Form(obj=usuario, id_usuario_editado=id_usuario)
    if formulario.validate_on_submit():
        formulario.populate_obj(usuario)
        usuario_service.editar_usuario(usuario, formulario.nueva_contraseña.data)
    return redirect("/")

@usuario_bp.post("/eliminar/<int:id_usuario>")
@check("usuarios_eliminar")
def eliminar_usuario(id_usuario:int):
    '''
    Elimina un usuario.
    
    Args:
        id_usuario (int): El id del usuario a eliminar.
        
    Returns:
        redirect: Redirige a la lista de usuarios.
    '''
    usuario_service.eliminar_usuario(id_usuario)
    flash('El usuario se ha eliminado correctamente', 'success')
    return redirect("/usuarios")

@usuario_bp.get("/recuperar")
def recuperar_contraseña():
    """
    Muestra el formulario para recuperar la contraseña.
    """
    formulario = RecuperarContraseñaForm()
    return render_template("usuarios/recuperar_contraseña.html", formulario=formulario)

@usuario_bp.post("/recuperar")
def procesar_recuperacion():
    """
    Procesa la solicitud de recuperación de contraseña.
    """
    formulario = RecuperarContraseñaForm()
    if formulario.validate_on_submit():
        user = usuario_service.recuperar_contraseña(formulario) 
        if user:
            #enviar_correo_recuperacion(user)  # Función que envía el correo con el token
            flash("Te hemos enviado un correo con tu nueva contraseña.", "info")
            return redirect(url_for("auth.login"))
        else:
            flash("El correo no está registrado en nuestro sistema.", "danger")
    return render_template("auth/recuperar_contraseña.html", formulario=formulario)

