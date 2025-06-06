FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo el código fuente de la API
COPY ./Api_Internacional /code

# Ejecuta desde el archivo main.py que está en /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
