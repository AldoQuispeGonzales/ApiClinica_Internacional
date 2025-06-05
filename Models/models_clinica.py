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
    tipo_afiliacion = Column(Integer)
    documento = Column(String)
    telefono = Column(String)
    correo = Column(String)

class Medico(Base):
    __tablename__ = "data_medico"
    medico_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    especialidad_id = Column(Integer)
    sucursal_id = Column(Integer)
    titulo_profesional_id = Column(Integer)
    estado = Column(String)
    correo = Column(String)
    empleado_id = Column(Integer)

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

class MetodoPago(Base):
    __tablename__ = "data_metodopago"
    metodo_pago_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

class Procedimiento(Base):
    __tablename__ = "data_procedimiento"
    procedimiento_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tipo = Column(String)
    descripcion = Column(String)

class Medicamento(Base):
    __tablename__ = "data_medicamento"
    medicamento_id = Column(Integer, primary_key=True, index=True)
    nombre_comercial = Column(String)
    principio_activo = Column(String)
    forma = Column(String)
    laboratorio = Column(String)

class TipoAfiliacion(Base):
    __tablename__ = "data_tipoafiliacion"
    tipo_afiliacion_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

class TipoCita(Base):
    __tablename__ = "data_tipocita"
    tipo_cita_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

class Turno(Base):
    __tablename__ = "data_turno"
    turno_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

class TipoTransaccionFinanciera(Base):
    __tablename__ = "data_tipotransaccionfinanciera"
    tipo_transaccion_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)

class TituloProfesional(Base):
    __tablename__ = "data_tituloprofesional"
    titulo_id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    tipo_titulo = Column(String)

class Empleado(Base):
    __tablename__ = "data_empleado"
    empleado_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    titulo_id = Column(Integer)
    estado = Column(String)
    rol = Column(String)

# Tabla de hechos
class CitaMedicaFact(Base):
    __tablename__ = "cita_medica_fact"
    cita_id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer)
    medico_id = Column(Integer)
    fecha_id = Column(Integer)
    especialidad_id = Column(Integer)
    sucursal_id = Column(Integer)
    servicio_id = Column(Integer)
    canal_atencion_id = Column(Integer)
    prioridad_cita_id = Column(Integer)
    diagnostico_id = Column(Integer)
    equipo_medico_id = Column(Integer)
    procedimiento_id = Column(Integer)

class PagoFact(Base):
    __tablename__ = "pago_fact"
    pago_id = Column(Integer, primary_key=True, index=True)
    cita_id = Column(Integer)
    paciente_id = Column(Integer)
    monto = Column(Float)
    fecha_pago = Column(Date)
    metodo_pago_id = Column(Integer)
    seguro_id = Column(Integer)

class EmpleadoAsistenciaFact(Base):
    __tablename__ = "empleado_asistencia_fact"
    asistencia_id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer)
    fecha_id = Column(Integer)
    sucursal_id = Column(Integer)
    canal_atencion_id = Column(Integer)
    hora_entrada = Column(Time)
    hora_salida = Column(Time)

class FinanzasFact(Base):
    __tablename__ = "finanzas_fact"
    finanza_id = Column(Integer, primary_key=True, index=True)
    fecha_finanza = Column(Date)
    sucursal_id = Column(Integer)
    servicio_id = Column(Integer)
    metodo_pago_id = Column(Integer)
    seguro_id = Column(Integer)
    tipo_movimiento = Column(String)
    monto = Column(Float)
