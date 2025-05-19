import pandas as pd
import psycopg2
from psycopg2 import sql

# Parámetros de conexión
conn = psycopg2.connect(
    host="localhost",
    database="DVZ_Internacional",
    user="admin",
    password="admin123",
    port=5432
)

cur = conn.cursor()


# Función para cargar CSV a tabla
def cargar_csv_a_postgres(nombre_archivo, nombre_tabla):
    df = pd.read_csv(nombre_archivo)

    # Crear tabla (DROP si existe)
    columnas = ", ".join([
        f"{col} {inferir_tipo_postgres(df[col])}"
        for col in df.columns
    ])

    cur.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(nombre_tabla)))
    cur.execute(sql.SQL("CREATE TABLE {} ({})").format(
        sql.Identifier(nombre_tabla),
        sql.SQL(columnas)
    ))

    # Insertar datos fila por fila
    for _, row in df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        cur.execute(
            sql.SQL("INSERT INTO {} VALUES ({})").format(
                sql.Identifier(nombre_tabla),
                sql.SQL(placeholders)
            ),
            tuple(row)
        )
    conn.commit()
    print(f"✅ Tabla '{nombre_tabla}' cargada con éxito.")


# Función para inferir tipos de datos en PostgreSQL
def inferir_tipo_postgres(serie):
    if pd.api.types.is_integer_dtype(serie):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(serie):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(serie):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(serie):
        return "TIMESTAMP"
    else:
        return "TEXT"


# Lista de archivos y tablas correspondientes
archivos_tablas = [
    ("Data_Fecha.csv", "data_fecha"),
    ("Data_Paciente.csv", "data_paciente"),
    ("Data_Medico.csv", "data_medico"),
    ("Data_Especialidad.csv", "data_especialidad"),
    ("Data_Sucursal.csv", "data_sucursal"),
    ("Data_Servicio.csv", "data_servicio"),
    ("Data_Pago.csv", "data_pago"),
    ("Data_Diagnostico.csv", "data_diagnostico"),
    ("Data_CanalAtencion.csv", "data_canalatencion"),
    ("Data_PrioridadCita.csv", "data_prioridadcita"),
    ("Data_Horario.csv", "data_horario"),
    ("Data_EquipoMedico.csv", "data_equipomedico"),
    ("Data_Seguro.csv", "data_seguro"),
    ("Cita_Medica_Fact.csv", "cita_medica_fact")
]

# Cargar todos los CSV a PostgreSQL
for archivo, tabla in archivos_tablas:
    cargar_csv_a_postgres(archivo, tabla)

# Cierre de conexión
cur.close()
conn.close()
