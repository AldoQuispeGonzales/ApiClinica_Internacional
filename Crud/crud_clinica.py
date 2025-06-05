from sqlalchemy.orm import Session
from Models import models_clinica as Models
from Schemas import schemas_clinica as Schemas

# ---------------- DIMENSIONES ----------------

def crear_paciente(db: Session, paciente: Schemas.PacienteCreate):
    db_paciente = Models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def obtener_pacientes(db: Session):
    return db.query(Models.Paciente).all()

def crear_canal_atencion(db: Session, canal: Schemas.CanalAtencionCreate):
    db_canal = Models.CanalAtencion(**canal.dict())
    db.add(db_canal)
    db.commit()
    db.refresh(db_canal)
    return db_canal

def obtener_canales_atencion(db: Session):
    return db.query(Models.CanalAtencion).all()

def crear_diagnostico(db: Session, diagnostico: Schemas.DiagnosticoCreate):
    db_diagnostico = Models.Diagnostico(**diagnostico.dict())
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico

def obtener_diagnosticos(db: Session):
    return db.query(Models.Diagnostico).all()

def crear_empleado(db: Session, empleado: Schemas.EmpleadoCreate):
    db_empleado = Models.Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def obtener_empleados(db: Session):
    return db.query(Models.Empleado).all()

def crear_equipo_medico(db: Session, equipo: Schemas.EquipoMedicoCreate):
    db_equipo = Models.EquipoMedico(**equipo.dict())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

def obtener_equipos_medicos(db: Session):
    return db.query(Models.EquipoMedico).all()

def crear_especialidad(db: Session, especialidad: Schemas.EspecialidadCreate):
    db_especialidad = Models.Especialidad(**especialidad.dict())
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad

def obtener_especialidades(db: Session):
    return db.query(Models.Especialidad).all()

def crear_fecha(db: Session, fecha: Schemas.FechaCreate):
    db_fecha = Models.Fecha(**fecha.dict())
    db.add(db_fecha)
    db.commit()
    db.refresh(db_fecha)
    return db_fecha

def obtener_fechas(db: Session):
    return db.query(Models.Fecha).all()

def crear_medicamento(db: Session, medicamento: Schemas.MedicamentoCreate):
    db_medicamento = Models.Medicamento(**medicamento.dict())
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento

def obtener_medicamentos(db: Session):
    return db.query(Models.Medicamento).all()

def crear_medico(db: Session, medico: Schemas.MedicoCreate):
    db_medico = Models.Medico(**medico.dict())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

def obtener_medicos(db: Session):
    return db.query(Models.Medico).all()

def crear_metodo_pago(db: Session, metodo: Schemas.MetodoPagoCreate):
    db_metodo = Models.MetodoPago(**metodo.dict())
    db.add(db_metodo)
    db.commit()
    db.refresh(db_metodo)
    return db_metodo

def obtener_metodos_pago(db: Session):
    return db.query(Models.MetodoPago).all()

def crear_prioridad_cita(db: Session, prioridad: Schemas.PrioridadCitaCreate):
    db_prioridad = Models.PrioridadCita(**prioridad.dict())
    db.add(db_prioridad)
    db.commit()
    db.refresh(db_prioridad)
    return db_prioridad

def obtener_prioridades_cita(db: Session):
    return db.query(Models.PrioridadCita).all()

def crear_procedimiento(db: Session, procedimiento: Schemas.ProcedimientoCreate):
    db_procedimiento = Models.Procedimiento(**procedimiento.dict())
    db.add(db_procedimiento)
    db.commit()
    db.refresh(db_procedimiento)
    return db_procedimiento

def obtener_procedimientos(db: Session):
    return db.query(Models.Procedimiento).all()

def crear_seguro(db: Session, seguro: Schemas.SeguroCreate):
    db_seguro = Models.Seguro(**seguro.dict())
    db.add(db_seguro)
    db.commit()
    db.refresh(db_seguro)
    return db_seguro

def obtener_seguros(db: Session):
    return db.query(Models.Seguro).all()

def crear_servicio(db: Session, servicio: Schemas.ServicioCreate):
    db_servicio = Models.Servicio(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def obtener_servicios(db: Session):
    return db.query(Models.Servicio).all()

def crear_sucursal(db: Session, sucursal: Schemas.SucursalCreate):
    db_sucursal = Models.Sucursal(**sucursal.dict())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

def obtener_sucursales(db: Session):
    return db.query(Models.Sucursal).all()

def crear_tipo_afiliacion(db: Session, tipo: Schemas.TipoAfiliacionCreate):
    db_tipo = Models.TipoAfiliacion(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def obtener_tipos_afiliacion(db: Session):
    return db.query(Models.TipoAfiliacion).all()

def crear_tipo_cita(db: Session, tipo: Schemas.TipoCitaCreate):
    db_tipo = Models.TipoCita(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def obtener_tipos_cita(db: Session):
    return db.query(Models.TipoCita).all()

def crear_tipo_transaccion(db: Session, tipo: Schemas.TipoTransaccionFinancieraCreate):
    db_tipo = Models.TipoTransaccionFinanciera(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def obtener_tipos_transaccion(db: Session):
    return db.query(Models.TipoTransaccionFinanciera).all()

def crear_titulo_profesional(db: Session, titulo: Schemas.TituloProfesionalCreate):
    db_titulo = Models.TituloProfesional(**titulo.dict())
    db.add(db_titulo)
    db.commit()
    db.refresh(db_titulo)
    return db_titulo

def obtener_titulos_profesionales(db: Session):
    return db.query(Models.TituloProfesional).all()

def crear_turno(db: Session, turno: Schemas.TurnoCreate):
    db_turno = Models.Turno(**turno.dict())
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

def obtener_turnos(db: Session):
    return db.query(Models.Turno).all()

def crear_pago_fact(db: Session, pago: Schemas.PagoFactCreate):
    db_pago = Models.PagoFact(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

def obtener_pagos_fact(db: Session):
    return db.query(Models.PagoFact).all()

def crear_empleado_asistencia_fact(db: Session, asistencia: Schemas.EmpleadoAsistenciaFactCreate):
    db_asistencia = Models.EmpleadoAsistenciaFact(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

def obtener_empleados_asistencia_fact(db: Session):
    return db.query(Models.EmpleadoAsistenciaFact).all()

def crear_finanzas_fact(db: Session, finanzas: Schemas.FinanzasFactCreate):
    db_finanzas = Models.FinanzasFact(**finanzas.dict())
    db.add(db_finanzas)
    db.commit()
    db.refresh(db_finanzas)
    return db_finanzas

def obtener_finanzas_fact(db: Session):
    return db.query(Models.FinanzasFact).all()

def crear_cita_medica_fact(db: Session, cita: Schemas.CitaMedicaFactCreate):
    db_cita = Models.CitaMedicaFact(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def obtener_citas_medicas_fact(db: Session):
    return db.query(Models.CitaMedicaFact).all()
