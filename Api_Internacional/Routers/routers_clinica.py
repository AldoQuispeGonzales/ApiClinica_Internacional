from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.database import get_db
from Crud.crud_clinica import (
    crear_paciente, obtener_pacientes,
    crear_medico, obtener_medicos,
    crear_especialidad, obtener_especialidades,
    crear_sucursal, obtener_sucursales,
    crear_servicio, obtener_servicios,
    crear_pago, obtener_pagos,
    crear_diagnostico, obtener_diagnosticos,
    crear_canal_atencion, obtener_canales_atencion,
    crear_prioridad_cita, obtener_prioridades_cita,
    crear_horario, obtener_horarios,
    crear_equipo_medico, obtener_equipos_medicos,
    crear_seguro, obtener_seguros,
    crear_fecha, obtener_fechas,
    crear_cita_medica_fact, obtener_citas_medicas_fact
)
from Schemas import schemas_clinica as schema

router = APIRouter()

# --- POST endpoints (crear) ---
@router.post("/pacientes/")
def crear_paciente_endpoint(paciente: schema.PacienteCreate, db: Session = Depends(get_db)):
    return crear_paciente(db, paciente)

@router.post("/medicos/")
def crear_medico_endpoint(medico: schema.MedicoCreate, db: Session = Depends(get_db)):
    return crear_medico(db, medico)

@router.post("/especialidades/")
def crear_especialidad_endpoint(especialidad: schema.EspecialidadCreate, db: Session = Depends(get_db)):
    return crear_especialidad(db, especialidad)

@router.post("/sucursales/")
def crear_sucursal_endpoint(sucursal: schema.SucursalCreate, db: Session = Depends(get_db)):
    return crear_sucursal(db, sucursal)

@router.post("/servicios/")
def crear_servicio_endpoint(servicio: schema.ServicioCreate, db: Session = Depends(get_db)):
    return crear_servicio(db, servicio)

@router.post("/pagos/")
def crear_pago_endpoint(pago: schema.PagoCreate, db: Session = Depends(get_db)):
    return crear_pago(db, pago)

@router.post("/diagnosticos/")
def crear_diagnostico_endpoint(diagnostico: schema.DiagnosticoCreate, db: Session = Depends(get_db)):
    return crear_diagnostico(db, diagnostico)

@router.post("/canales-atencion/")
def crear_canal_atencion_endpoint(canal: schema.CanalAtencionCreate, db: Session = Depends(get_db)):
    return crear_canal_atencion(db, canal)

@router.post("/prioridades-cita/")
def crear_prioridad_cita_endpoint(prioridad: schema.PrioridadCitaCreate, db: Session = Depends(get_db)):
    return crear_prioridad_cita(db, prioridad)

@router.post("/horarios/")
def crear_horario_endpoint(horario: schema.HorarioCreate, db: Session = Depends(get_db)):
    return crear_horario(db, horario)

@router.post("/equipos-medicos/")
def crear_equipo_medico_endpoint(equipo: schema.EquipoMedicoCreate, db: Session = Depends(get_db)):
    return crear_equipo_medico(db, equipo)

@router.post("/seguros/")
def crear_seguro_endpoint(seguro: schema.SeguroCreate, db: Session = Depends(get_db)):
    return crear_seguro(db, seguro)

@router.post("/fechas/")
def crear_fecha_endpoint(fecha: schema.FechaCreate, db: Session = Depends(get_db)):
    return crear_fecha(db, fecha)

@router.post("/citas-medicas/")
def crear_cita_medica_endpoint(cita: schema.CitaMedicaFactCreate, db: Session = Depends(get_db)):
    return crear_cita_medica_fact(db, cita)

# --- GET endpoints (obtener todos) ---

@router.get("/pacientes/")
def obtener_pacientes_endpoint(db: Session = Depends(get_db)):
    return obtener_pacientes(db)

@router.get("/medicos/")
def obtener_medicos_endpoint(db: Session = Depends(get_db)):
    return obtener_medicos(db)

@router.get("/especialidades/")
def obtener_especialidades_endpoint(db: Session = Depends(get_db)):
    return obtener_especialidades(db)

@router.get("/sucursales/")
def obtener_sucursales_endpoint(db: Session = Depends(get_db)):
    return obtener_sucursales(db)

@router.get("/servicios/")
def obtener_servicios_endpoint(db: Session = Depends(get_db)):
    return obtener_servicios(db)

@router.get("/pagos/")
def obtener_pagos_endpoint(db: Session = Depends(get_db)):
    return obtener_pagos(db)

@router.get("/diagnosticos/")
def obtener_diagnosticos_endpoint(db: Session = Depends(get_db)):
    return obtener_diagnosticos(db)

@router.get("/canales-atencion/")
def obtener_canales_atencion_endpoint(db: Session = Depends(get_db)):
    return obtener_canales_atencion(db)

@router.get("/prioridades-cita/")
def obtener_prioridades_cita_endpoint(db: Session = Depends(get_db)):
    return obtener_prioridades_cita(db)

@router.get("/horarios/")
def obtener_horarios_endpoint(db: Session = Depends(get_db)):
    return obtener_horarios(db)

@router.get("/equipos-medicos/")
def obtener_equipos_medicos_endpoint(db: Session = Depends(get_db)):
    return obtener_equipos_medicos(db)

@router.get("/seguros/")
def obtener_seguros_endpoint(db: Session = Depends(get_db)):
    return obtener_seguros(db)

@router.get("/fechas/")
def obtener_fechas_endpoint(db: Session = Depends(get_db)):
    return obtener_fechas(db)

@router.get("/citas-medicas/")
def obtener_citas_medicas_endpoint(db: Session = Depends(get_db)):
    return obtener_citas_medicas_fact(db)
