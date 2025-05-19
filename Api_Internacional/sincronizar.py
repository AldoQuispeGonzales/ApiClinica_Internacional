import psycopg2
import pymysql
from urllib.parse import urlparse

# Conexión local PostgreSQL
DATABASE_URL = "postgresql://admin:admin123@localhost:5432/DVZ_Internacional"

def parse_db_url(db_url):
    result = urlparse(db_url)
    return {
        "dbname": result.path[1:],
        "user": result.username,
        "password": result.password,
        "host": result.hostname,
        "port": result.port
    }

# Conexión remota MySQL
config_remota = pymysql.connect(
    host="us-imm-web465.main-hosting.eu",
    user="u777467137_deviozapp",
    password="Deviozapp10+",
    database="u777467137_deviozapp"
)

# Mapeo de tablas: {tabla_local_pgsql: tabla_remota_mysql}
tabla_mapeo = {
    'cita_medica_fact': 'pract_07_Cita_Medica_Fact',
    'data_canalatencion': 'pract_07_Data_CanalAtencion',
    'data_diagnostico': 'pract_07_Data_Diagnostico',
    'data_equipomedico': 'pract_07_Data_EquipoMedico',
    'data_especialidad': 'pract_07_Data_Especialidad',
    'data_fecha': 'pract_07_Data_Fecha',
    'data_horario': 'pract_07_Data_Horario',
    'data_medico': 'pract_07_Data_Medico',
    'data_paciente': 'pract_07_Data_Paciente',
    'data_pago': 'pract_07_Data_Pago',
    'data_prioridadcita': 'pract_07_Data_PrioridadCita',
    'data_seguro': 'pract_07_Data_Seguro',
    'data_servicio': 'pract_07_Data_Servicio',
    'data_sucursal': 'pract_07_Data_Sucursal'
}

try:
    conn_pg = psycopg2.connect(**parse_db_url(DATABASE_URL))
    cursor_pg = conn_pg.cursor()
    cursor_mysql = config_remota.cursor()

    for tabla_local, tabla_remota in tabla_mapeo.items():
        cursor_pg.execute(f'SELECT * FROM "{tabla_local}"')
        rows = cursor_pg.fetchall()
        columns = [desc[0] for desc in cursor_pg.description]

        # Eliminar contenido previo en la tabla remota
        cursor_mysql.execute(f'DELETE FROM `{tabla_remota}`')

        if rows:
            placeholders = ", ".join(["%s"] * len(columns))
            column_names = ", ".join([f"`{col}`" for col in columns])
            insert_query = f'INSERT INTO `{tabla_remota}` ({column_names}) VALUES ({placeholders})'
            cursor_mysql.executemany(insert_query, rows)
            print(f"✔ Tabla '{tabla_remota}' sincronizada con {len(rows)} registros.")

    config_remota.commit()

except Exception as e:
    print("❌ Error durante sincronización:", e)

finally:
    cursor_pg.close()
    conn_pg.close()
    cursor_mysql.close()
    config_remota.close()
