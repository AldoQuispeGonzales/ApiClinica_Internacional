from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.database import get_db
from Crud.crud_clinica import *
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

@router.post("/diagnosticos/")
def crear_diagnostico_endpoint(diagnostico: schema.DiagnosticoCreate, db: Session = Depends(get_db)):
    return crear_diagnostico(db, diagnostico)

@router.post("/canales-atencion/")
def crear_canal_atencion_endpoint(canal: schema.CanalAtencionCreate, db: Session = Depends(get_db)):
    return crear_canal_atencion(db, canal)

@router.post("/prioridades-cita/")
def crear_prioridad_cita_endpoint(prioridad: schema.PrioridadCitaCreate, db: Session = Depends(get_db)):
    return crear_prioridad_cita(db, prioridad)

@router.post("/equipos-medicos/")
def crear_equipo_medico_endpoint(equipo: schema.EquipoMedicoCreate, db: Session = Depends(get_db)):
    return crear_equipo_medico(db, equipo)

@router.post("/seguros/")
def crear_seguro_endpoint(seguro: schema.SeguroCreate, db: Session = Depends(get_db)):
    return crear_seguro(db, seguro)

@router.post("/fechas/")
def crear_fecha_endpoint(fecha: schema.FechaCreate, db: Session = Depends(get_db)):
    return crear_fecha(db, fecha)

@router.post("/medicamentos/")
def crear_medicamento_endpoint(medicamento: schema.MedicamentoCreate, db: Session = Depends(get_db)):
    return crear_medicamento(db, medicamento)

@router.post("/empleados/")
def crear_empleado_endpoint(empleado: schema.EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, empleado)

@router.post("/metodos-pago/")
def crear_metodo_pago_endpoint(metodo: schema.MetodoPagoCreate, db: Session = Depends(get_db)):
    return crear_metodo_pago(db, metodo)

@router.post("/procedimientos/")
def crear_procedimiento_endpoint(procedimiento: schema.ProcedimientoCreate, db: Session = Depends(get_db)):
    return crear_procedimiento(db, procedimiento)

@router.post("/tipo-afiliacion/")
def crear_tipo_afiliacion_endpoint(tipo: schema.TipoAfiliacionCreate, db: Session = Depends(get_db)):
    return crear_tipo_afiliacion(db, tipo)

@router.post("/tipo-cita/")
def crear_tipo_cita_endpoint(tipo: schema.TipoCitaCreate, db: Session = Depends(get_db)):
    return crear_tipo_cita(db, tipo)

@router.post("/turnos/")
def crear_turno_endpoint(turno: schema.TurnoCreate, db: Session = Depends(get_db)):
    return crear_turno(db, turno)

@router.post("/tipo-transaccion/")
def crear_tipo_transaccion_endpoint(tipo: schema.TipoTransaccionFinancieraCreate, db: Session = Depends(get_db)):
    return crear_tipo_transaccion(db, tipo)

@router.post("/titulos-profesionales/")
def crear_titulo_profesional_endpoint(titulo: schema.TituloProfesionalCreate, db: Session = Depends(get_db)):
    return crear_titulo_profesional(db, titulo)

@router.post("/citas-medicas/")
def crear_cita_medica_endpoint(cita: schema.CitaMedicaFactCreate, db: Session = Depends(get_db)):
    return crear_cita_medica_fact(db, cita)

@router.post("/pagos-fact/")
def crear_pago_fact_endpoint(pago: schema.PagoFactCreate, db: Session = Depends(get_db)):
    return crear_pago_fact(db, pago)

@router.post("/asistencias-empleado/")
def crear_empleado_asistencia_endpoint(asistencia: schema.EmpleadoAsistenciaFactCreate, db: Session = Depends(get_db)):
    return crear_empleado_asistencia_fact(db, asistencia)

@router.post("/finanzas/")
def crear_finanzas_endpoint(finanzas: schema.FinanzasFactCreate, db: Session = Depends(get_db)):
    return crear_finanzas_fact(db, finanzas)

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

@router.get("/diagnosticos/")
def obtener_diagnosticos_endpoint(db: Session = Depends(get_db)):
    return obtener_diagnosticos(db)

@router.get("/canales-atencion/")
def obtener_canales_atencion_endpoint(db: Session = Depends(get_db)):
    return obtener_canales_atencion(db)

@router.get("/prioridades-cita/")
def obtener_prioridades_cita_endpoint(db: Session = Depends(get_db)):
    return obtener_prioridades_cita(db)

@router.get("/equipos-medicos/")
def obtener_equipos_medicos_endpoint(db: Session = Depends(get_db)):
    return obtener_equipos_medicos(db)

@router.get("/seguros/")
def obtener_seguros_endpoint(db: Session = Depends(get_db)):
    return obtener_seguros(db)

@router.get("/fechas/")
def obtener_fechas_endpoint(db: Session = Depends(get_db)):
    return obtener_fechas(db)

@router.get("/medicamentos/")
def obtener_medicamentos_endpoint(db: Session = Depends(get_db)):
    return obtener_medicamentos(db)

@router.get("/empleados/")
def obtener_empleados_endpoint(db: Session = Depends(get_db)):
    return obtener_empleados(db)

@router.get("/metodos-pago/")
def obtener_metodos_pago_endpoint(db: Session = Depends(get_db)):
    return obtener_metodos_pago(db)

@router.get("/procedimientos/")
def obtener_procedimientos_endpoint(db: Session = Depends(get_db)):
    return obtener_procedimientos(db)

@router.get("/tipo-afiliacion/")
def obtener_tipos_afiliacion_endpoint(db: Session = Depends(get_db)):
    return obtener_tipos_afiliacion(db)

@router.get("/tipo-cita/")
def obtener_tipos_cita_endpoint(db: Session = Depends(get_db)):
    return obtener_tipos_cita(db)

@router.get("/turnos/")
def obtener_turnos_endpoint(db: Session = Depends(get_db)):
    return obtener_turnos(db)

@router.get("/tipo-transaccion/")
def obtener_tipos_transaccion_endpoint(db: Session = Depends(get_db)):
    return obtener_tipos_transaccion(db)

@router.get("/titulos-profesionales/")
def obtener_titulos_profesionales_endpoint(db: Session = Depends(get_db)):
    return obtener_titulos_profesionales(db)

@router.get("/citas-medicas/")
def obtener_citas_medicas_endpoint(db: Session = Depends(get_db)):
    return obtener_citas_medicas_fact(db)

@router.get("/pagos-fact/")
def obtener_pagos_fact_endpoint(db: Session = Depends(get_db)):
    return obtener_pagos_fact(db)

@router.get("/asistencias-empleado/")
def obtener_empleados_asistencia_endpoint(db: Session = Depends(get_db)):
    return obtener_empleados_asistencia_fact(db)

@router.get("/finanzas/")
def obtener_finanzas_endpoint(db: Session = Depends(get_db)):
    return obtener_finanzas_fact(db)
