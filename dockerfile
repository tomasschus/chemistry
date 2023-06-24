# Utiliza una imagen base de Python
FROM python:3.10

# Establece un directorio de trabajo en /usr/src/app
WORKDIR /usr/src/app

# Copia los archivos de requerimientos e instala los requerimientos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el directorio actual en el contenedor en /usr/src/app
COPY . .

# Ejecuta tu programa Python
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

