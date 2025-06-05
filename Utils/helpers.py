def formatear_respuesta(data, mensaje="Operación exitosa"):
    return {
        "mensaje": mensaje,
        "data": data
    }

def validar_id_entero(id_str: str) -> int:
    try:
        return int(id_str)
    except ValueError:
        raise ValueError("ID inválido. Debe ser un número entero.")
