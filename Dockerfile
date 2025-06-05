FROM python:3.11-slim

# Evita archivos .pyc y salida con buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /code

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY ./App ./App

# Puerto requerido por Render
EXPOSE 10000

# Comando para arrancar la app
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "10000"]
