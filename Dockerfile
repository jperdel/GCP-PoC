# Imagen base oficial de Python
FROM python:3.11

# Evita logs innecesarios y mejora comportamiento
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos dependencias primero (mejor caching)
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY app/ app/

# Cloud Run escucha siempre en $PORT
ENV PORT=8080

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]