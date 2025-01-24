from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.core.models.postulacion.programa import Programa
from src.core.services import programa_service
from src.web.forms.programa import ProgramaForm

bp = Blueprint('programa', __name__, url_prefix='/programas')  

@bp.get('/crear_programa')
def crear_programa():
    form = ProgramaForm()
    return render_template('programas/crear_programa.html', form=form)

@bp.post('/guardar_programa')
def guardar_programa():
    form = ProgramaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        if not nombre:
            flash('El nombre es requerido', 'danger')
            return redirect(url_for('programa.crear_programa'))
        programa_service.crear_programa(nombre)
        return redirect(url_for('programa.listar_programas'))
    flash('Error al guardar el programa', 'danger')
    return render_template('programas/crear_programa.html', form=form)

@bp.get('/listar_programas')
def listar_programas():
    programas = programa_service.listar_programas()
    return render_template('programas/listar_programas.html', programas=programas)

@bp.get('/editar_programa/<int:id>')
def editar_programa(id):
    programa = programa_service.get_programa_by_id(id)
    form = ProgramaForm(obj=programa)
    return render_template('programas/editar_programa.html', form=form, id=id)

@bp.post('/actualizar_programa/<int:id>')
def actualizar_programa(id):
    form = ProgramaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        if not nombre:
            flash('El nombre es requerido', 'danger')
            return redirect(url_for('programa.editar_programa', id=id))
        programa_service.actualizar_programa(id, nombre)
        return redirect(url_for('programa.listar_programas'))
    flash('Error al actualizar el programa', 'danger')
    return redirect(url_for('programa.editar_programa', id=id))

@bp.post('/eliminar_programa/<int:id>')
def eliminar_programa(id):
    programa_service.eliminar_programa(id)
    return redirect(url_for('programa.listar_programas'))

    