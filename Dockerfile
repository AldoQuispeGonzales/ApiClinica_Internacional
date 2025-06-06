# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /code

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Comando por defecto para ejecutar
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
