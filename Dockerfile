# Usar Python como imagen base
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente
COPY . .

# Moverse a la carpeta donde está manage.py antes de ejecutar comandos
WORKDIR /app/api

# Exponer el puerto en el que se ejecutará Django
EXPOSE 8000

# Comando para ejecutar migraciones y levantar el servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
