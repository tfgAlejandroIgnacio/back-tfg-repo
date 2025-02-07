
# 🚀 Funcionamiento de los Endpoints de la API

## 📌 Requisitos Previos

Primero debes tener iniciado el servidor de **Python** con la API.  
Si no lo has hecho, revisa primero el archivo **README.md** principal.

---

## 🌐 URL Base del Servidor

```
http://127.0.0.1:8000/
```

> **Nota:** Esta es la URL por defecto. Si has cambiado el puerto, ajusta la URL correspondiente.

---

## 🛠️ Aplicaciones de la API

### 1. **📂 Categoría**

Los campos de **categoría** son:

- `id`
- `nombre`

#### 🔄 Operaciones CRUD:

- **GET todas las categorías**  
  **URL:** `http://127.0.0.1:8000/categoria`  
  **Método:** `GET`  
  **Respuesta:** Devuelve un array con todas las categorías.  
  **Código de Respuesta:** `302_FOUND`

---

- **GET categoría por ID**  
  **URL:** `http://127.0.0.1:8000/categoria/<id>`  
  **Método:** `GET`  
  **Respuestas Posibles:**  
  - `404_NOT_FOUND` si la categoría no existe  
  - `302_FOUND` con el JSON de la categoría si se encuentra

---

- **POST (Crear nueva categoría)**  
  **URL:** `http://127.0.0.1:8000/categoria`  
  **Método:** `POST`  
  **Respuesta:**  
  - `201_CREATED` si se crea correctamente  
  - `400_BAD_REQUEST` si hay un error en la solicitud  

  **Ejemplo de JSON para crear una categoría:**
  ```json
  {
      "nombre": "Frutas"
  }
  ```

> ⚠️ **Importante:** Asegúrate de enviar el contenido en formato **JSON**.

---

- **DELETE (Eliminar categoría)**  
  **URL:** `http://127.0.0.1:8000/categoria/<id>`  
  **Método:** `DELETE`  
  **Respuestas Posibles:**  
  - `202_ACCEPTED` si la categoría se elimina correctamente  
  - `404_NOT_FOUND` si la categoría no existe  

---

> ❌ **Nota:** El método **PUT (actualización)** no está implementado para categorías.

---

### 2. **📦 Producto**

Los campos de **producto** son:

- `id`
- `nombre`
- `stock`
- `categoria`

> **Nota:**  
> - En **GET**, el campo `categoria` mostrará todos sus atributos.  
> - En **POST/PUT**, solo necesitas especificar el `id_categoria`.

---

#### 🔄 Operaciones CRUD:

- **GET todos los productos**  
  **URL:** `http://127.0.0.1:8000/producto`  
  **Método:** `GET`  
  **Respuesta:** Devuelve un array con todos los productos.

---

- **GET producto por ID**  
  **URL:** `http://127.0.0.1:8000/producto/<id>`  
  **Método:** `GET`  
  **Respuesta:** Devuelve el producto específico.

---

- **POST (Crear nuevo producto)**  
  **URL:** `http://127.0.0.1:8000/producto`  
  **Método:** `POST`  
  **Ejemplo de JSON:**
  ```json
  {
      "nombre": "manzana",
      "stock": 200,
      "id_categoria": 1
  }
  ```

---

- **DELETE (Eliminar producto)**  
  **URL:** `http://127.0.0.1:8000/producto/<id>`  
  **Método:** `DELETE`  
  **Respuestas Posibles:**  
  - `200_OK` si el producto se elimina correctamente  
  - `404_NOT_FOUND` si el producto no existe  

---

- **PUT (Actualizar producto)**  
  **URL:** `http://127.0.0.1:8000/producto/<id>`  
  **Método:** `PUT`  
  **Ejemplo de JSON:**
  ```json
  {
      "nombre": "Manzana",
      "stock": 100,
      "id_categoria": 2
  }
  ```

  **Respuestas Posibles:**  
  - `200_OK` si la modificación fue exitosa  
  - `304_NOT_MODIFIED` si ocurrió un error  
  - `404_NOT_FOUND` si el producto no existe  

---
