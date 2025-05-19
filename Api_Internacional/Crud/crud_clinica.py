from sqlalchemy.orm import Session
from Models import models_clinica as Models
from Schemas import schemas_clinica as Schemas

# ---------------- DIMENSIONES ----------------

# Paciente
def crear_paciente(db: Session, paciente: Schemas.PacienteCreate):
    db_paciente = Models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def obtener_pacientes(db: Session):
    return db.query(Models.Paciente).all()

# Medico
def crear_medico(db: Session, medico: Schemas.MedicoCreate):
    db_medico = Models.Medico(**medico.dict())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

def obtener_medicos(db: Session):
    return db.query(Models.Medico).all()

# Especialidad
def crear_especialidad(db: Session, especialidad: Schemas.EspecialidadCreate):
    db_especialidad = Models.Especialidad(**especialidad.dict())
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad

def obtener_especialidades(db: Session):
    return db.query(Models.Especialidad).all()

# Sucursal
def crear_sucursal(db: Session, sucursal: Schemas.SucursalCreate):
    db_sucursal = Models.Sucursal(**sucursal.dict())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

def obtener_sucursales(db: Session):
    return db.query(Models.Sucursal).all()

# Servicio
def crear_servicio(db: Session, servicio: Schemas.ServicioCreate):
    db_servicio = Models.Servicio(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def obtener_servicios(db: Session):
    return db.query(Models.Servicio).all()

# Diagnostico
def crear_diagnostico(db: Session, diagnostico: Schemas.DiagnosticoCreate):
    db_diagnostico = Models.Diagnostico(**diagnostico.dict())
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico

def obtener_diagnosticos(db: Session):
    return db.query(Models.Diagnostico).all()

# Canal Atencion
def crear_canal_atencion(db: Session, canal: Schemas.CanalAtencionCreate):
    db_canal = Models.CanalAtencion(**canal.dict())
    db.add(db_canal)
    db.commit()
    db.refresh(db_canal)
    return db_canal

def obtener_canales_atencion(db: Session):
    return db.query(Models.CanalAtencion).all()

# Prioridad Cita
def crear_prioridad_cita(db: Session, prioridad: Schemas.PrioridadCitaCreate):
    db_prioridad = Models.PrioridadCita(**prioridad.dict())
    db.add(db_prioridad)
    db.commit()
    db.refresh(db_prioridad)
    return db_prioridad

def obtener_prioridades_cita(db: Session):
    return db.query(Models.PrioridadCita).all()

# Horario
def crear_horario(db: Session, horario: Schemas.HorarioCreate):
    db_horario = Models.Horario(**horario.dict())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

def obtener_horarios(db: Session):
    return db.query(Models.Horario).all()

# Equipo Medico
def crear_equipo_medico(db: Session, equipo: Schemas.EquipoMedicoCreate):
    db_equipo = Models.EquipoMedico(**equipo.dict())
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)
    return db_equipo

def obtener_equipos_medicos(db: Session):
    return db.query(Models.EquipoMedico).all()

# Seguro
def crear_seguro(db: Session, seguro: Schemas.SeguroCreate):
    db_seguro = Models.Seguro(**seguro.dict())
    db.add(db_seguro)
    db.commit()
    db.refresh(db_seguro)
    return db_seguro

def obtener_seguros(db: Session):
    return db.query(Models.Seguro).all()

# Fecha
def crear_fecha(db: Session, fecha: Schemas.FechaCreate):
    db_fecha = Models.Fecha(**fecha.dict())
    db.add(db_fecha)
    db.commit()
    db.refresh(db_fecha)
    return db_fecha

def obtener_fechas(db: Session):
    return db.query(Models.Fecha).all()

# Pago
def crear_pago(db: Session, pago: Schemas.PagoCreate):
    db_pago = Models.Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

def obtener_pagos(db: Session):
    return db.query(Models.Pago).all()

# ---------------- TABLA DE HECHOS ----------------

# Cita Medica
def crear_cita_medica_fact(db: Session, cita: Schemas.CitaMedicaFactCreate):
    db_cita = Models.CitaMedicaFact(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def obtener_citas_medicas_fact(db: Session):
    return db.query(Models.CitaMedicaFact).all()
