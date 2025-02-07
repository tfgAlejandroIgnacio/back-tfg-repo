# 🎯 back-tfg-repo
**Repositorio oficial del backend del TFG**  

## 📥 Descarga de la API

### ✅ Requisitos previos:
Necesitas tener lo siguiente:
- 📂 **Repositorio de GitHub clonado**
- 🛢️ **Base de datos MySQL llamada `main`**

---

### 🔹 Paso 1: Crear entorno virtual
Ejecuta el siguiente comando para iniciar un nuevo entorno virtual:  
```bash
python3 -m venv venv
```

Después, actívalo con:  
```bash
source venv/bin/activate
```

---

### 🔹 Paso 2: Instalar dependencias
1. 📂 **Ve a la carpeta del proyecto (no la aplicación).**  
2. 📜 Ejecuta `ls` para asegurarte de que estás en la carpeta correcta (debes ver el archivo `requirements.txt`).  
3. Instala todas las dependencias necesarias con:  
   ```bash
   pip install -r requirements.txt
   ```

---

### 🔹 Paso 3: Aplicar migraciones
📌 En la misma carpeta donde está `requirements.txt`, ejecuta:  
```bash
python realizar_migraciones.py
```
🔍 **Revisa que las migraciones sean correctas.**

---

### 🚀 Paso 4: Ejecutar el servidor
Ejecuta el siguiente comando para iniciar el servidor:  
```bash
python manage.py runserver
```

🎉 ¡Listo! Ahora tu API debería estar en funcionamiento. 🚀  