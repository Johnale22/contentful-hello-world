# Usamos Python Slim para una imagen ligera
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos solo el archivo de requerimientos primero (Cache layer optimization)
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY app.py .

# Comando de ejecución
CMD ["python", "app.py"]