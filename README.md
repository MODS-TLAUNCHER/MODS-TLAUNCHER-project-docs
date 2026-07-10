# Persona 4 — Core del proyecto, UI global e integración

## Backend
- `backend/biUNestar/settings.py` — Configuración general (apps instaladas, BD, static/media, seguridad)
- `backend/biUNestar/urls.py` — Rutas raíz (admin, login/logout, password reset, e incluye las rutas de las otras 3 apps)
- `backend/biUNestar/wsgi.py`, `backend/biUNestar/asgi.py` — Entrada de despliegue
- `backend/manage.py` — CLI de Django
- `backend/requirements.txt` — Dependencias
- `backend/clean_student_ids.py`, `backend/setup_fix.py`, `backend/setup.bat` — Scripts de utilidades/instalación
- `backend/.env.example` — Plantilla de variables de entorno

## Frontend
- `frontend/templates/base.html` — Plantilla base (navbar, layout, bloques que heredan las demás páginas)
- `frontend/templates/dashboard.html` — Vista principal que integra hábitos y recursos
- `frontend/static/custom.css` — Estilos globales
- `frontend/static/custom.js` — Interactividad general (JS del lado del cliente)

## Notas
Esta persona es responsable de:
1. Que el proyecto arranque de punta a punta (`python manage.py runserver`)
2. Integrar las ramas `feature/accounts`, `feature/habits`, `feature/resources` al repo principal
3. Resolver conflictos de merge, sobre todo en `templates/base.html` y `biUNestar/urls.py`
