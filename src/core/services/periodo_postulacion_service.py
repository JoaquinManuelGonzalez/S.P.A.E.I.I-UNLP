from src.core.models.postulacion.periodo_postulacion import PeriodoPostulacion
from src.core.database import db
from src.core.models.postulacion.estado import Estado
from src.core.models.postulacion.postulacion import Postulacion
from src.core.services import postulacion_service
from sqlalchemy import or_, and_
from datetime import datetime


def periodo_actual(): #Devuelve el periodo de postulacion actual, si existe, el cual es unico
    periodo_actual = db.session.query(PeriodoPostulacion).filter(
            PeriodoPostulacion.inicio <= datetime.now(),
            (PeriodoPostulacion.fin == None) | (PeriodoPostulacion.fin >= datetime.now())
        ).first()
    if periodo_actual: return periodo_actual
    
    print("No existe un periodo activo actualmente.")
    return None

def habilitar_periodo_postulacion(inicio = None): #Habilita un nuevo periodo de postulacion
    periodo = periodo_actual()
    if periodo:
        print("No se puede habilitar un nuevo periodo de inscripciones sin cerrar primero el activo.")
        return None
    
    if inicio:
        periodo_nuevo = PeriodoPostulacion(inicio=inicio)
    else:
        periodo_nuevo = PeriodoPostulacion()
    db.session.add(periodo_nuevo)
    db.session.commit()
    
    cancelar_postulaciones_pendientes()

    return periodo_nuevo

def deshabilitar_periodo_postulacion(): #Deshabilita el periodo de postulacion actual
    periodo = periodo_actual()
    if periodo:
        periodo.fin = datetime.now()
    else:
        print("No hay periodo actual activo que deshabilitar.")
    db.session.commit()

def cancelar_postulaciones_pendientes():
    postulaciones = db.session.query(Postulacion).filter(
        or_(
            ~Postulacion.estado.has(Estado.nombre.ilike(f"%Postulacion Aceptada%")),
            ~Postulacion.estado.has(Estado.nombre.ilike(f"%Postulacion Completada%")),
            ~Postulacion.estado.has(Estado.nombre.ilike(f"%Postulacion Finalizada%")),
            ~Postulacion.estado.has(Estado.nombre.ilike(f"%Postulacion en Espera de ser Completada%"))
        )
    )
    for postulacion in postulaciones:
        postulacion_service.actualizar_estado_postulacion(postulacion, "Postulacion Cancelada o Interrumpida")
    return    

def listar_periodos_postulacion(inicio=None, fin=None, pagina=1, por_pagina=10, orden=None):
    """
    Lista los periodos de postulacion segun ciertos filtros, paginado.
    """
    periodos = PeriodoPostulacion.query
    if inicio:
        periodos = periodos.filter(PeriodoPostulacion.inicio >= inicio)
    if fin:
        periodos = periodos.filter(
            or_(
            PeriodoPostulacion.fin == None,
            PeriodoPostulacion.fin <= fin
            )
        )
    if orden == "asc":
        periodos = periodos.order_by(PeriodoPostulacion.inicio.asc())
    else:
        periodos = periodos.order_by(PeriodoPostulacion.inicio.desc())
    return periodos.paginate(page=pagina, per_page=por_pagina, error_out=False)

def listar_periodos_postulacion_completo():
    """
    Lista TODOS los periodos de postulacion.
    """

    
    return PeriodoPostulacion.query.all()

def get_periodo_postulacion_by_id(id_periodo):
    """
    Obtiene un periodo de postulación por su id.
    """
    return PeriodoPostulacion.query.get(id_postulacion)

"""
def verificar_validez(fecha_inicio, fecha_fin):
    periodos_existentes = PeriodoPostulacion.query

    #Un periodo A es invalido si existe otro periodo B tal que:
    #A comienza antes de que B termine
    #AND
    #A termina despues de que B empiece
    if fecha_fin:
        periodos_existentes = periodos_existentes.filter( 
            and_(
                PeriodoPostulacion.fecha_fin >= fecha_inicio,
                or_(
                PeriodoPostulacion.fin == None,
                PeriodoPostulacion.fin >= fecha_inicio
                )
            )
        )
    else:  #si no hay fecha_fin, entonces el periodo no termina, entonces SIEMPRE termina luego de que B empiece
        periodos_existentes = periodos_existentes.filter(
            or_(
                PeriodoPostulacion.fin == None,
                PeriodoPostulacion.fin >= fecha_inicio
            )
        )
    return periodos_existentes
    """

            

def esta_activo():
    return periodo_actual() != None