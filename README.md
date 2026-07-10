# biUNestar

# 👽 MODS (TLAUNCHER) - Repositorio "Ingeniería de Software I"

Este repositorio contiene todas las entregas y desarrollo del proyecto biUNestar para la asignatura de Ingeniería de Software I.

*Semestre:* 2026-I

## El grupo 🔥🛰️🔥

| Integrante | Carrera | Correo |
|---|---|---|
| CASTIBLANCO CASTAÑEDA PEDRO ALEJANDRO | Ingeniería en sistemas y computación | pcastblanco@unal.edu.co |
| QUIÑONES SEGURA JAIME JAVIER ANDRES | Ingeniería en sistemas y computación | jquinoness@unal.edu.co |
| AGUDELO PARRA DANIEL FELIPE | Ingeniería en sistemas y computación | daagudelop@unal.edu.co |
| OMAR ANDRES QUIÑONES MEJIA | Ingeniería en sistemas y computación | oquinones@unal.edu.co |

# Descripción del proyecto

biUNestar es una aplicación diseñada para apoyar a los estudiantes en el cuidado de su bienestar emocional y sus hábitos diarios, permitiendo registrar y gestionar aspectos relacionados con su salud y calidad de vida.

# Estructura del proyecto

## Backend

- `backend/biUNestar/settings.py` — Configuración general (apps instaladas, BD, static/media y seguridad).
- `backend/biUNestar/urls.py` — Rutas principales del proyecto (admin, login/logout, recuperación de contraseña e integración de aplicaciones).
- `backend/biUNestar/wsgi.py`, `backend/biUNestar/asgi.py` — Archivos de entrada para despliegue.
- `backend/manage.py` — CLI de Django.
- `backend/requirements.txt` — Dependencias del proyecto.
- `backend/clean_student_ids.py`, `backend/setup_fix.py`, `backend/setup.bat` — Scripts de instalación y utilidades.
- `backend/.env.example` — Plantilla de variables de entorno.

## Frontend

- `frontend/templates/base.html` — Plantilla base con navbar, estructura general y bloques reutilizables.
- `frontend/templates/dashboard.html` — Vista principal que integra hábitos y recursos.
- `frontend/static/custom.css` — Estilos globales.
- `frontend/static/custom.js` — Interactividad del lado del cliente.

# Responsabilidades de integración

Esta parte del proyecto se encarga de:

1. Garantizar que la aplicación pueda ejecutarse correctamente (`python manage.py runserver`).
2. Integrar las ramas del proyecto (`feature/accounts`, `feature/habits`, `feature/resources`) al repositorio principal.
3. Resolver conflictos de integración, especialmente en archivos compartidos como:
   - `templates/base.html`
   - `biUNestar/urls.py`