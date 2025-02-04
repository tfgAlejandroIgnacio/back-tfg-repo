import os
import subprocess
from django.db import connection

def delete_migrations():
    # Eliminar archivos de migraciones
    for root, dirs, files in os.walk("."):
        if "migrations" in dirs:
            migrations_dir = os.path.join(root, "migrations")
            print(f"Eliminando migraciones en: {migrations_dir}")
            for file in os.listdir(migrations_dir):
                if file != "__init__.py":
                    file_path = os.path.join(migrations_dir, file)
                    os.remove(file_path)
                    print(f"Eliminado: {file_path}")

def reset_django_migrations_table():
    # Eliminar registros de la tabla django_migrations
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM django_migrations;")
    print("Tabla django_migrations reseteada.")

def run_migrations(apps):
    # Crear y aplicar migraciones para las aplicaciones especificadas
    for app in apps:
        print(f"Creando migraciones para: {app}")
        subprocess.run(["python", "manage.py", "makemigrations", app])
    
    print("Aplicando migraciones...")
    subprocess.run(["python", "manage.py", "migrate"])

if __name__ == "__main__":
    # Aplicaciones que deseas migrar
    apps_to_migrate = ["categoria", "producto", "pedido", "detalles_pedido", "cocinero"]

    # Paso 1: Eliminar migraciones anteriores
    delete_migrations()

    # Paso 2: Resetear la tabla django_migrations
    reset_django_migrations_table()

    # Paso 3: Crear y aplicar nuevas migraciones
    run_migrations(apps_to_migrate)

    print("¡Proceso completado!")