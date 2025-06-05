from pydantic import BaseModel
from typing import Optional
from datetime import date, time

# --- Dimensiones ---
class Fecha(BaseModel):
    fecha_id: int
    fecha: date
    anio: int
    trimestre: int
    mes: int
    nombre_dia: str
    class Config:
        from_attributes = True

class Paciente(BaseModel):
    paciente_id: int
    nombre: str
    genero: str
    fecha_nacimiento: date
    edad: int
    tipo_afiliacion: int
    documento: str
    telefono: str
    correo: str
    class Config:
        from_attributes = True

class Medico(BaseModel):
    medico_id: int
    nombre: str
    especialidad_id: int
    sucursal_id: int
    titulo_profesional_id: int
    estado: str
    correo: str
    empleado_id: int
    class Config:
        from_attributes = True

class Especialidad(BaseModel):
    especialidad_id: int
    nombre: str
    descripcion: Optional[str]
    tipo: Optional[str]
    class Config:
        from_attributes = True

class Sucursal(BaseModel):
    sucursal_id: int
    nombre: str
    direccion: str
    distrito: str
    ciudad: str
    class Config:
        from_attributes = True

class Servicio(BaseModel):
    servicio_id: int
    nombre_servicio: str
    categoria: str
    modo: str
    class Config:
        from_attributes = True

class Diagnostico(BaseModel):
    diagnostico_id: int
    codigo_cie10: str
    descripcion: Optional[str]
    class Config:
        from_attributes = True

class CanalAtencion(BaseModel):
    canal_id: int
    descripcion: str
    class Config:
        from_attributes = True

class PrioridadCita(BaseModel):
    prioridad_id: int
    nivel: str
    descripcion: Optional[str]
    class Config:
        from_attributes = True

class EquipoMedico(BaseModel):
    equipo_medico_id: int
    nombre_equipo: str
    tipo_equipo: str
    estado_equipo: str
    fabricante: str
    class Config:
        from_attributes = True

class Seguro(BaseModel):
    seguro_id: int
    nombre_seguro: str
    tipo_seguro: str
    cobertura_porcentaje: float
    class Config:
        from_attributes = True

class Medicamento(BaseModel):
    medicamento_id: int
    nombre_comercial: str
    principio_activo: str
    forma: str
    laboratorio: str
    class Config:
        from_attributes = True

class Procedimiento(BaseModel):
    procedimiento_id: int
    nombre: str
    tipo: str
    descripcion: str
    class Config:
        from_attributes = True

class MetodoPago(BaseModel):
    metodo_pago_id: int
    descripcion: str
    class Config:
        from_attributes = True

class TipoAfiliacion(BaseModel):
    tipo_afiliacion_id: int
    descripcion: str
    class Config:
        from_attributes = True

class TipoCita(BaseModel):
    tipo_cita_id: int
    descripcion: str
    class Config:
        from_attributes = True

class Turno(BaseModel):
    turno_id: int
    nombre: str
    class Config:
        from_attributes = True

class TipoTransaccionFinanciera(BaseModel):
    tipo_transaccion_id: int
    descripcion: str
    class Config:
        from_attributes = True

class TituloProfesional(BaseModel):
    titulo_id: int
    descripcion: str
    tipo_titulo: str
    class Config:
        from_attributes = True

class Empleado(BaseModel):
    empleado_id: int
    nombre: str
    titulo_id: int
    estado: str
    rol: str
    class Config:
        from_attributes = True

# --- Hechos ---
class CitaMedicaFact(BaseModel):
    cita_id: int
    paciente_id: int
    medico_id: int
    fecha_id: int
    especialidad_id: int
    sucursal_id: int
    servicio_id: int
    canal_atencion_id: int
    prioridad_cita_id: int
    diagnostico_id: int
    equipo_medico_id: int
    procedimiento_id: int
    class Config:
        from_attributes = True

class PagoFact(BaseModel):
    pago_id: int
    cita_id: int
    paciente_id: int
    monto: float
    fecha_pago: date
    metodo_pago_id: int
    seguro_id: int
    class Config:
        from_attributes = True

class EmpleadoAsistenciaFact(BaseModel):
    asistencia_id: int
    empleado_id: int
    fecha_id: int
    sucursal_id: int
    canal_atencion_id: int
    hora_entrada: time
    hora_salida: time
    class Config:
        from_attributes = True

class FinanzasFact(BaseModel):
    finanza_id: int
    fecha_finanza: date
    sucursal_id: int
    servicio_id: int
    metodo_pago_id: int
    seguro_id: int
    tipo_movimiento: str
    monto: float
    class Config:
        from_attributes = True

# --- Schemas para creación (Create) ---
class FechaCreate(BaseModel):
    fecha: date
    anio: int
    trimestre: int
    mes: int
    nombre_dia: str

class PacienteCreate(BaseModel):
    nombre: str
    genero: str
    fecha_nacimiento: date
    edad: int
    tipo_afiliacion: int
    documento: str
    telefono: str
    correo: str

class MedicoCreate(BaseModel):
    nombre: str
    especialidad_id: int
    sucursal_id: int
    titulo_profesional_id: int
    estado: str
    correo: str
    empleado_id: int

class EspecialidadCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    tipo: Optional[str] = None

class SucursalCreate(BaseModel):
    nombre: str
    direccion: str
    distrito: str
    ciudad: str

class ServicioCreate(BaseModel):
    nombre_servicio: str
    categoria: str
    modo: str

class DiagnosticoCreate(BaseModel):
    codigo_cie10: str
    descripcion: Optional[str] = None

class CanalAtencionCreate(BaseModel):
    descripcion: str

class PrioridadCitaCreate(BaseModel):
    nivel: str
    descripcion: Optional[str] = None

class EquipoMedicoCreate(BaseModel):
    nombre_equipo: str
    tipo_equipo: str
    estado_equipo: str
    fabricante: str

class SeguroCreate(BaseModel):
    nombre_seguro: str
    tipo_seguro: str
    cobertura_porcentaje: float

class MedicamentoCreate(BaseModel):
    nombre_comercial: str
    principio_activo: str
    forma: str
    laboratorio: str

class ProcedimientoCreate(BaseModel):
    nombre: str
    tipo: str
    descripcion: str

class MetodoPagoCreate(BaseModel):
    descripcion: str

class TipoAfiliacionCreate(BaseModel):
    descripcion: str

class TipoCitaCreate(BaseModel):
    descripcion: str

class TurnoCreate(BaseModel):
    nombre: str

class TipoTransaccionFinancieraCreate(BaseModel):
    descripcion: str

class TituloProfesionalCreate(BaseModel):
    descripcion: str
    tipo_titulo: str

class EmpleadoCreate(BaseModel):
    nombre: str
    titulo_id: int
    estado: str
    rol: str

class CitaMedicaFactCreate(BaseModel):
    paciente_id: int
    medico_id: int
    fecha_id: int
    especialidad_id: int
    sucursal_id: int
    servicio_id: int
    canal_atencion_id: int
    prioridad_cita_id: int
    diagnostico_id: int
    equipo_medico_id: int
    procedimiento_id: int

class PagoFactCreate(BaseModel):
    cita_id: int
    paciente_id: int
    monto: float
    fecha_pago: date
    metodo_pago_id: int
    seguro_id: int

class EmpleadoAsistenciaFactCreate(BaseModel):
    empleado_id: int
    fecha_id: int
    sucursal_id: int
    canal_atencion_id: int
    hora_entrada: time
    hora_salida: time

class FinanzasFactCreate(BaseModel):
    fecha_finanza: date
    sucursal_id: int
    servicio_id: int
    metodo_pago_id: int
    seguro_id: int
    tipo_movimiento: str
    monto: float
