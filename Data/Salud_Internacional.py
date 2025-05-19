import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('es_ES')
random.seed(42)

# Parámetros
N_PACIENTES = 5000
N_MEDICOS = 500
N_FECHAS = 3 * 365
N_SUCURSALES = 5
N_SERVICIOS = 30
N_PAGOS = 10000
N_DIAGNOSTICOS = 500
N_ESPECIALIDADES = 60
N_EQUIPOS = 100
N_SEGUROS = 10
N_HORARIOS = 24
N_CANALES = 4
N_PRIORIDADES = 3
N_CITAS = 15000

# --------- Dimensiones ---------

# Data_Fecha
start_date = datetime.strptime("2022-01-01", "%Y-%m-%d")
fechas = []
for i in range(N_FECHAS):
    fecha = start_date + timedelta(days=i)
    fechas.append({
        "fecha_id": i+1,
        "fecha": fecha.date(),
        "anio": fecha.year,
        "mes": fecha.month,
        "trimestre": (fecha.month - 1) // 3 + 1,
        "nombre_dia": fecha.strftime("%A")
    })
df_fecha = pd.DataFrame(fechas)

# Data_Paciente
df_paciente = pd.DataFrame([{
    "paciente_id": i+1,
    "nombre": fake.name(),
    "genero": random.choice(["Masculino", "Femenino"]),
    "fecha_nacimiento": fake.date_of_birth(minimum_age=0, maximum_age=90),
    "edad": 0,  # se calculará luego
    "tipo_afiliacion": random.choice(["Particular", "EPS", "Seguro Privado", "SIS"]),
    "documento": f"{random.randint(10000000, 99999999)}",
    "telefono": fake.phone_number(),
    "correo": fake.email()
} for i in range(N_PACIENTES)])
df_paciente["edad"] = df_paciente["fecha_nacimiento"].apply(lambda x: 2025 - x.year)

# Data_Medico
especialidades = [
    "Cardiología", "Pediatría", "Ginecología", "Dermatología", "Endocrinología", "Gastroenterología",
    "Nefrología", "Neurología", "Oncología", "Oftalmología", "Otorrinolaringología", "Traumatología",
    "Urología", "Reumatología", "Psicología", "Psiquiatría", "Medicina General", "Medicina Interna",
    "Cirugía General", "Cirugía Plástica", "Cirugía Cardiovascular", "Cirugía Pediátrica", "Neumología",
    "Alergología", "Nutrición", "Infectología", "Fisioterapia", "Odontología", "Geriatría", "Hematología"
]
especialidades += [f"Especialidad {i}" for i in range(len(especialidades)+1, N_ESPECIALIDADES+1)]

df_especialidad = pd.DataFrame({
    "especialidad_id": range(1, len(especialidades)+1),
    "nombre": especialidades,
    "descripcion": [f"Atención en {esp}" for esp in especialidades],
    "tipo": [random.choice(["Médica", "Quirúrgica", "Diagnóstica", "Terapéutica"]) for _ in especialidades]
})

df_medico = pd.DataFrame([{
    "medico_id": i+1,
    "nombre": fake.name(),
    "especialidad": random.choice(especialidades),
    "turno": random.choice(["Mañana", "Tarde", "Noche"]),
    "estado": random.choice(["Activo", "Inactivo"]),
    "nro_colegiatura": f"COL-{random.randint(10000,99999)}"
} for i in range(N_MEDICOS)])

# Data_Sucursal
df_sucursal = pd.DataFrame([{
    "sucursal_id": i+1,
    "nombre": f"Sucursal {i+1}",
    "direccion": fake.address(),
    "distrito": fake.city(),
    "ciudad": "Lima"
} for i in range(N_SUCURSALES)])

# Data_Servicio
df_servicio = pd.DataFrame([{
    "servicio_id": i+1,
    "nombre_servicio": f"Servicio {i+1}",
    "categoria": random.choice(["Consulta", "Procedimiento", "Examen", "Hospitalización"]),
    "modo": random.choice(["Presencial", "Virtual"])
} for i in range(N_SERVICIOS)])

# Data_Pago
df_pago = pd.DataFrame([{
    "pago_id": i+1,
    "metodo_pago": random.choice(["Efectivo", "Tarjeta", "Transferencia", "Seguro"]),
    "total": round(random.uniform(50, 1500), 2),
    "descuento": round(random.uniform(0, 300), 2),
    "copago": round(random.uniform(0, 100), 2),
    "fecha_pago": fake.date_between(start_date='-2y', end_date='today'),
    "estado_pago": random.choice(["Pagado", "Pendiente", "Anulado"])
} for i in range(N_PAGOS)])

# Data_Diagnostico (simulado)
df_diagnostico = pd.DataFrame([{
    "diagnostico_id": i+1,
    "codigo_cie10": f"{random.choice('ABCDEFGHI')}{random.randint(0,99):02}",
    "descripcion": fake.sentence(nb_words=4)
} for i in range(N_DIAGNOSTICOS)])

# Data_CanalAtencion
df_canal = pd.DataFrame({
    "canal_id": range(1, N_CANALES+1),
    "descripcion": ["Presencial", "Web", "Teléfono", "App Móvil"]
})

# Data_PrioridadCita
df_prioridad = pd.DataFrame({
    "prioridad_id": [1, 2, 3],
    "nivel": ["Baja", "Media", "Alta"],
    "descripcion": ["Control o rutina", "Síntomas moderados", "Emergencia"]
})

# Data_Horario
df_horario = pd.DataFrame([{
    "horario_id": i+1,
    "hora_inicio": f"{i:02}:00",
    "hora_fin": f"{(i+1)%24:02}:00",
    "turno": random.choice(["Mañana", "Tarde", "Noche"])
} for i in range(N_HORARIOS)])

# Data_EquipoMedico
df_equipo = pd.DataFrame([{
    "equipo_medico_id": i+1,
    "nombre_equipo": f"{random.choice(['Ecógrafo', 'Rayos X', 'Monitor'])} {i+1}",
    "tipo_equipo": random.choice(["Diagnóstico", "Quirúrgico"]),
    "estado_equipo": random.choice(["Operativo", "En mantenimiento", "Fuera de servicio"]),
    "fabricante": fake.company()
} for i in range(N_EQUIPOS)])

# Data_Seguro
df_seguro = pd.DataFrame([{
    "seguro_id": i+1,
    "nombre_seguro": f"Seguro {i+1}",
    "tipo_seguro": random.choice(["Público", "Privado"]),
    "cobertura_porcentaje": random.choice([70, 80, 90, 100])
} for i in range(N_SEGUROS)])

# --------- Hechos: Cita_Medica_Fact ---------

import pandas as pd
import random

df_cita = pd.DataFrame([{
    "id_cita": i + 1,
    "fecha_id": random.randint(1, N_FECHAS),
    "paciente_id": random.randint(1, N_PACIENTES),
    "medico_id": random.randint(1, N_MEDICOS),
    "servicio_id": random.randint(1, N_SERVICIOS),
    "sucursal_id": random.randint(1, N_SUCURSALES),
    "diagnostico_id": random.randint(1, N_DIAGNOSTICOS),
    "pago_id": random.randint(1, N_PAGOS),
    "especialidad_id": random.randint(1, N_ESPECIALIDADES),
    "equipo_medico_id": random.randint(1, N_EQUIPOS),
    "seguro_id": random.randint(1, N_SEGUROS),
    "horario_id": random.randint(1, N_HORARIOS),
    "canal_id": random.randint(1, N_CANALES),
    "prioridad_id": random.randint(1, N_PRIORIDADES),
    "duracion_min": random.choice([15, 30, 45, 60]),
    "estado_cita": random.choice(["Completada", "Cancelada", "Reprogramada", "Pendiente"])
} for i in range(N_CITAS)])


# --------- Guardar como CSV ---------
df_fecha.to_csv("Data_Fecha.csv", index=False)
df_paciente.to_csv("Data_Paciente.csv", index=False)
df_medico.to_csv("Data_Medico.csv", index=False)
df_especialidad.to_csv("Data_Especialidad.csv", index=False)
df_sucursal.to_csv("Data_Sucursal.csv", index=False)
df_servicio.to_csv("Data_Servicio.csv", index=False)
df_pago.to_csv("Data_Pago.csv", index=False)
df_diagnostico.to_csv("Data_Diagnostico.csv", index=False)
df_canal.to_csv("Data_CanalAtencion.csv", index=False)
df_prioridad.to_csv("Data_PrioridadCita.csv", index=False)
df_horario.to_csv("Data_Horario.csv", index=False)
df_equipo.to_csv("Data_EquipoMedico.csv", index=False)
df_seguro.to_csv("Data_Seguro.csv", index=False)
df_cita.to_csv("Cita_Medica_Fact.csv", index=False)

# ----------------------------- # crear una coneion BD
# ----------------------------- # crear tablas de estos parametros D,E
# ----------------------------- # insertar data del csv generado a postgreSQL

