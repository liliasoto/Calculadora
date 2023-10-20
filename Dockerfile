# Usa una imagen base de Python
FROM python:3.9.18-slim-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia tu aplicación y archivos adicionales (si los tienes) al directorio de trabajo
COPY . /app

# Instala las dependencias si es necesario
# RUN pip install -r requirements.txt

# Especifica el comando a ejecutar cuando se inicie el contenedor
CMD [ "python", "calculadora.py" ]
