from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.core.models.postulacion.programa import Programa
from src.core.services import programa_service
from src.web.forms.programa import ProgramaForm
from src.web.handlers.permisos import check

bp = Blueprint('programa', __name__, url_prefix='/programas')  


@bp.get('/crear_programa')
@check('admin')
def crear_programa():
    form = ProgramaForm()
    return render_template('programas/crear_programa.html', form=form)

@bp.post('/guardar_programa')
@check('admin')
def guardar_programa():
    form = ProgramaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        habilitado = form.habilitado.data
        if not nombre:
            flash('El nombre es requerido', 'danger')
            return redirect(url_for('programa.crear_programa'))
        programa_service.crear_programa(nombre, habilitado)
        return redirect(url_for('programa.listar_programas'))
    flash('Error al guardar el programa', 'danger')
    return render_template('programas/crear_programa.html', form=form)

@bp.get('/listar_programas')
@check('admin')
def listar_programas():
    programas = programa_service.listar_programas()
    return render_template('programas/listar_programas.html', programas=programas)

@bp.get('/editar_programa/<int:id>')
@check('admin')
def editar_programa(id):
    programa = programa_service.get_programa_by_id(id)
    form = ProgramaForm(obj=programa)
    return render_template('programas/editar_programa.html', form=form, id=id)

@bp.post('/actualizar_programa/<int:id>')
@check('admin')
def actualizar_programa(id):
    form = ProgramaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        habilitado = form.habilitado.data
        if not nombre:
            flash('El nombre es requerido', 'danger')
            return redirect(url_for('programa.editar_programa', id=id))
        programa_service.actualizar_programa(id, nombre, habilitado)
        return redirect(url_for('programa.listar_programas'))
    flash('Error al actualizar el programa', 'danger')
    return redirect(url_for('programa.editar_programa', id=id))

@bp.post('/eliminar_programa/<int:id>')
@check('admin')
def eliminar_programa(id):
    programa_service.eliminar_programa(id)
    return redirect(url_for('programa.listar_programas'))

@bp.get('/cambiar_estado_programa/<int:id>')
@check('admin')
def cambiar_estado(id):
    programa = programa_service.get_programa_by_id(id)
    programa.habilitado = not programa.habilitado
    programa_service.actualizar_programa(programa.id, programa.nombre, programa.habilitado)
    flash('Estado actualizado correctamente', 'success')
    return redirect(url_for('programa.listar_programas'))

    