import os
import shutil
import subprocess
from pathlib import Path

apps = ["categoria", "producto", "pedido", "detalles_pedido", "cocinero"]

for app in apps:
    migrations_path = Path(app) / "migrations"
    
    if migrations_path.exists():
        for file in migrations_path.iterdir():
            if file.name != "__init__.py":
                if file.is_file():
                    file.unlink()
                elif file.is_dir():
                    shutil.rmtree(file)
        print(f"🗑️ Migraciones eliminadas en {app}")

# Generar migraciones
try:
    subprocess.run(["python", "manage.py", "makemigrations"], check=True)
    print("✅ Migraciones generadas con éxito")
except subprocess.CalledProcessError:
    print("❌ Error al generar migraciones. Revisa los modelos.")
    exit(1)

# Aplicar migraciones
try:
    subprocess.run(["python", "manage.py", "migrate"], check=True)
    print("🚀 Migraciones aplicadas con éxito")
except subprocess.CalledProcessError:
    print("❌ Error al aplicar migraciones.")
    exit(1)
