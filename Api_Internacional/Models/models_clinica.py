from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from App.database import Base

# Tabla de dimensiones
class Paciente(Base):
    __tablename__ = "data_paciente"
    paciente_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    genero = Column(String)
    fecha_nacimiento = Column(Date)
    edad = Column(Integer)
    tipo_afiliacion = Column(String)
    documento = Column(String)
    telefono = Column(String)
    correo = Column(String)

class Medico(Base):
    __tablename__ = "data_medico"
    medico_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    especialidad = Column(String)
    turno = Column(String)
    estado = Column(String)
    nro_colegiatura = Column(String)

class Especialidad(Base):
    __tablename__ = "data_especialidad"
    especialidad_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    tipo = Column(String)

class Diagnostico(Base):
    __tablename__ = "data_diagnostico"
    diagnostico_id = Column(Integer, primary_key=True, index=True)
    codigo_cie10 = Column(String)
    descripcion = Column(String)

class CanalAtencion(Base):
    __tablename__ = "data_canalatencion"
    canal_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

class PrioridadCita(Base):
    __tablename__ = "data_prioridadcita"
    prioridad_id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String)
    descripcion = Column(String)

class Horario(Base):
    __tablename__ = "data_horario"
    horario_id = Column(Integer, primary_key=True, index=True)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    turno = Column(String)

class EquipoMedico(Base):
    __tablename__ = "data_equipomedico"
    equipo_medico_id = Column(Integer, primary_key=True, index=True)
    nombre_equipo = Column(String)
    tipo_equipo = Column(String)
    estado_equipo = Column(String)
    fabricante = Column(String)

class Seguro(Base):
    __tablename__ = "data_seguro"
    seguro_id = Column(Integer, primary_key=True, index=True)
    nombre_seguro = Column(String)
    tipo_seguro = Column(String)
    cobertura_porcentaje = Column(Float)

class Sucursal(Base):
    __tablename__ = "data_sucursal"
    sucursal_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    distrito = Column(String)
    ciudad = Column(String)

class Servicio(Base):
    __tablename__ = "data_servicio"
    servicio_id = Column(Integer, primary_key=True, index=True)
    nombre_servicio = Column(String)
    categoria = Column(String)
    modo = Column(String)

class Fecha(Base):
    __tablename__ = "data_fecha"
    fecha_id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    anio = Column(Integer)
    mes = Column(Integer)
    trimestre = Column(Integer)
    nombre_dia = Column(String)

class Pago(Base):
    __tablename__ = "data_pago"
    pago_id = Column(Integer, primary_key=True, index=True)
    metodo_pago = Column(String)
    total = Column(Float)
    descuento = Column(Float)
    copago = Column(Float)
    fecha_pago = Column(Date)
    estado_pago = Column(String)

# Tabla de hechos
class CitaMedicaFact(Base):
    __tablename__ = "cita_medica_fact"
    id_cita = Column(Integer, primary_key=True, index=True)
    fecha_id = Column(Integer, ForeignKey("data_fecha.fecha_id"))
    paciente_id = Column(Integer, ForeignKey("data_paciente.paciente_id"))
    medico_id = Column(Integer, ForeignKey("data_medico.medico_id"))
    servicio_id = Column(Integer, ForeignKey("servicio.servicio_id"))
    sucursal_id = Column(Integer, ForeignKey("sucursal.sucursal_id"))
    diagnostico_id = Column(Integer, ForeignKey("diagnostico.diagnostico_id"))
    pago_id = Column(Integer, ForeignKey("data_pago.pago_id"))
    especialidad_id = Column(Integer, ForeignKey("especialidad.especialidad_id"))
    equipo_medico_id = Column(Integer, ForeignKey("equipo_medico.equipo_medico_id"))
    seguro_id = Column(Integer, ForeignKey("seguro.seguro_id"))
    horario_id = Column(Integer, ForeignKey("horario.horario_id"))
    canal_id = Column(Integer, ForeignKey("canal_atencion.canal_id"))
    prioridad_id = Column(Integer, ForeignKey("data_prioridadcita.prioridad_id"))
    duracion_min = Column(Integer)
    estado_cita = Column(String)
