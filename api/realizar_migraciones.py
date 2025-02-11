import os
import shutil

# Paso 1: Eliminar migraciones antiguas (excepto __init__.py)
apps = ["categoria", "producto", "pedido", "detalles_pedido", "cocinero"]
for app in apps:
    migrations_path = f"{app}/migrations"
    if os.path.exists(migrations_path):
        for file in os.listdir(migrations_path):
            file_path = os.path.join(migrations_path, file)
            if file != "__init__.py":
                if os.path.isfile(file_path):  # Si es archivo, eliminarlo
                    os.remove(file_path)
                elif os.path.isdir(file_path):  # Si es directorio, eliminarlo completamente
                    shutil.rmtree(file_path)
        print(f"🗑️ Migraciones eliminadas en {app}")

# Paso 2: Generar migraciones en orden
migrations_order = ["categoria", "producto", "cocinero", "pedido", "detalles_pedido"]
for app in migrations_order:
    os.system(f"python manage.py makemigrations {app}")
    print(f"✅ Migración generada para {app}")

# Paso 3: Aplicar las migraciones
os.system("python manage.py migrate")
print("🚀 Migraciones aplicadas con éxito")
