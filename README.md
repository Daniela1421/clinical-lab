# Clinical Lab – Sistema de laboratorio clínico 🧪

Aplicación web Full Stack para gestionar pacientes, órdenes médicas y exámenes clínicos.  
Incluye backend en **FastAPI + SQLAlchemy** y frontend en **Vue 3 + BootstrapVue**, siguiendo una arquitectura limpia y escalable.

---

## 🧩 Funcionalidades

### ✅ Backend (FastAPI + MySQL)
- Crear y consultar pacientes
- Crear órdenes de examen
- Asociar exámenes a una orden
- Listar órdenes por documento del paciente
- Ver detalle de cada orden
- Base de datos persistente con relaciones bien definidas

### ✅ Frontend (Vue 3 + BootstrapVue)
- Registro de pacientes
- Creación de órdenes (seleccionando exámenes)
- Búsqueda de órdenes por documento del paciente
- Visualización de detalle de orden (con modal)
- Interfaz sencilla, funcional y coherente

---


## 🚀 Cómo ejecutar el proyecto localmente

### 🔧 Requisitos
- Python 3.10+
- Node.js y npm
- Docker (opcional, pero recomendado para MySQL)

---

### 🔙 Backend (FastAPI)

# 1. Ir a la carpeta del backend
```
  cd backend
```

# 2. Crear entorno virtual e instalar dependencias
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

# 3. Configurar base de datos

# Opción A: Usar Docker (recomendado) ejecutar: 
```
docker-compose up -d
```

### Opción B: Tener MySQL instalado localmente (sin Docker)

1. Asegúrate de tener **MySQL Server** instalado en tu sistema.

2. Ejecuta el script SQL para crear la base de datos y las tablas. Desde la raíz del proyecto, ejecuta el siguiente comando:

  ```
    mysql -u tu_usuario_mysql -p < ./mysql-init/esquema_laboratorio_clinico.sql
  ```

Este script creará la base de datos, sus tablas y algunos datos de prueba.

3. Crea un archivo .env dentro de la carpeta backend/ con el siguiente contenido:

  ```
    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=tu_usuario_mysql
    DB_PASSWORD=tu_contraseña_mysql
    DB_NAME=laboratorio_clinico
  ```

# 4. Ejecutar el servidor
uvicorn app.main:app --reload

El backend estará corriendo en:
📡 http://localhost:8000

### 🔙 Frontend (Vue 3)

# 1. Ir a la carpeta del frontend
```
cd ../frontend
```

# 2. Instalar dependencias
```
npm install
```

# 3. Ejecutar el proyecto
```
npm run dev
```

La interfaz estará disponible en:
🌐 http://localhost:5173

## 🔗 Endpoints principales

- `POST /pacientes/`: Registrar paciente  
- `GET /pacientes/documento/{documento}`: Obtener paciente  
- `POST /ordenes/`: Crear orden  
- `GET /ordenes/paciente/{documento}`: Listar órdenes de un paciente  
- `GET /ordenes/{id}`: Detalle de una orden  
- `POST /ordenes-examenes/`: Asignar examen a orden  
- `GET /ordenes-examenes/orden/{id}`: Ver exámenes de una orden  
- `GET /examenes/`: Listar exámenes disponibles  
- `POST /examenes/`: Crear exámenes

---


## 🧠 Recomendaciones de mejora

- Estilos UX/UI más profesionales (tema clínico, iconografía, accesibilidad)
- Autenticación de usuarios
- Subida de resultados de exámenes
- Filtro por fechas y estado
- Dashboard resumen

---

## 👩‍💻 Autora

Daniela Ducuara  
