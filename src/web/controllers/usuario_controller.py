from flask import Blueprint, render_template, request, redirect, flash, url_for
from src.core.services import usuario_service, facultades as facultades_service
from src.web.handlers.permisos import check
from src.web.forms import Usuario_Form, Nueva_Contraseña_Form, RecuperarContraseñaForm

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
    facultades = facultades_service.listar_facultades()
    formulario.id_rol.choices = [("", "Seleccione un rol")] + [(rol.id, rol.nombre) for rol in roles if rol.nombre != "alumno" and rol.nombre != "presidencia_jefe"]
    formulario.facultad_id.choices = [("", "Seleccione una facultad")] + [(facultad.id, facultad.nombre) for facultad in facultades]
    if formulario.validate_on_submit():
        usuario_service.crear_usuario(formulario)
        return redirect("/usuarios")
    return render_template("usuarios/crear_usuario.html", formulario=formulario)

@usuario_bp.get("detalle/<int:id_usuario>")
@check("usuarios_detalle")
def ver_detalle_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    roles = usuario_service.listar_roles()
    facultades = facultades_service.listar_facultades()
    formulario = Usuario_Form(obj=usuario)
    formulario.id_rol.choices = [(rol.id, rol.nombre) for rol in roles]
    formulario.facultad_id.choices = [(facultad.id, facultad.nombre) for facultad in facultades]
    return render_template("usuarios/detalle_usuario.html", formulario=formulario, usuario=usuario)


@usuario_bp.route("/editar/<int:id_usuario>", methods=['POST'])
@check("usuarios_editar")   
def editar_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    formulario_usuario = Usuario_Form(obj=usuario, id_usuario_editado=id_usuario)
    formulario_contraseña = Nueva_Contraseña_Form()
    return render_template("usuarios/editar_usuario.html", formulario_usuario=formulario_usuario, formulario_contraseña=formulario_contraseña , usuario=usuario)

@usuario_bp.route("/actualizar/<int:id_usuario>", methods=['POST'])
@check("usuarios_editar")
def actualizar_usuario(id_usuario:int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    roles = usuario_service.listar_roles()
    formulario_usuario = Usuario_Form(obj=usuario, id_usuario_editado=id_usuario)
    formulario_usuario.id_rol.choices = [(rol.id, rol.nombre) for rol in roles]
    formulario_contraseña = Nueva_Contraseña_Form(request.form)
    if formulario_usuario.validate_on_submit() and formulario_contraseña.validate_on_submit():
        formulario_usuario.populate_obj(usuario)
        usuario_service.editar_usuario(usuario, formulario_contraseña.nueva_contraseña.data)
    else:
        return render_template("usuarios/editar_usuario.html", formulario_usuario=formulario_usuario, formulario_contraseña=formulario_contraseña , usuario=usuario)
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
    return redirect("/usuarios")

@usuario_bp.post("/reactivar/<int:id_usuario>")
@check("usuarios_eliminar")
def reactivar_usuario(id_usuario:int):
    '''
    Reactiva un usuario.
    
    Args:
        id_usuario (int): El id del usuario a reactivar.
        
    Returns:
        redirect: Redirige a la lista de usuarios.
    '''
    usuario_service.reactivar_usuario(id_usuario)
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
            return redirect(url_for("auth.login"))
        else:
            flash("El correo no está registrado en nuestro sistema.", "danger")
    return render_template("auth/recuperar_contraseña.html", formulario=formulario)

