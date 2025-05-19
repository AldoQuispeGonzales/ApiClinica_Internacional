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
    tipo_afiliacion: str
    documento: str
    telefono: str
    correo: str

    class Config:
        from_attributes = True

class Medico(BaseModel):
    medico_id: int
    nombre: str
    especialidad: str
    turno: str
    estado: str
    nro_colegiatura: str

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

class Pago(BaseModel):
    pago_id: int
    metodo_pago: str
    total: float
    descuento: float
    copago: float
    fecha_pago: date
    estado_pago: str

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

class Horario(BaseModel):
    horario_id: int
    hora_inicio: time
    hora_fin: time
    turno: str

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

# --- Hechos ---

class CitaMedicaFact(BaseModel):
    id_cita: int
    fecha_id: int
    paciente_id: int
    medico_id: int
    especialidad_id: int
    sucursal_id: int
    servicio_id: int
    pago_id: int
    diagnostico_id: int
    canal_id: int
    prioridad_id: int
    horario_id: int
    equipo_medico_id: int
    seguro_id: int
    duracion_min: int
    estado_cita: str

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
    tipo_afiliacion: str
    documento: str
    telefono: str
    correo: str

class MedicoCreate(BaseModel):
    nombre: str
    especialidad: str
    turno: str
    estado: str
    nro_colegiatura: str

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

class PagoCreate(BaseModel):
    metodo_pago: str
    total: float
    descuento: float
    copago: float
    fecha_pago: date
    estado_pago: str

class DiagnosticoCreate(BaseModel):
    codigo_cie10: str
    descripcion: Optional[str] = None

class CanalAtencionCreate(BaseModel):
    descripcion: str

class PrioridadCitaCreate(BaseModel):
    nivel: str
    descripcion: Optional[str] = None

class HorarioCreate(BaseModel):
    hora_inicio: time
    hora_fin: time
    turno: str

class EquipoMedicoCreate(BaseModel):
    nombre_equipo: str
    tipo_equipo: str
    estado_equipo: str
    fabricante: str

class SeguroCreate(BaseModel):
    nombre_seguro: str
    tipo_seguro: str
    cobertura_porcentaje: float

class CitaMedicaFactCreate(BaseModel):
    fecha_id: int
    paciente_id: int
    medico_id: int
    especialidad_id: int
    sucursal_id: int
    servicio_id: int
    pago_id: int
    diagnostico_id: int
    canal_id: int
    prioridad_id: int
    horario_id: int
    equipo_medico_id: int
    seguro_id: int
    duracion_min: int
    estado_cita: str
