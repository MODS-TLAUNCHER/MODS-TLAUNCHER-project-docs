@echo off
echo === Configurando biUNestar ===

echo 1. Creando entorno virtual...
python -m venv venv

echo 2. Activando entorno virtual...
call venv\Scripts\activate

echo 3. Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

echo 4. Ejecutando migraciones...
python manage.py makemigrations
python manage.py migrate

echo 5. Creando superusuario...
python manage.py createsuperuser

echo 6. Recopilando archivos estáticos...
python manage.py collectstatic --noinput

echo === Configuración completada ===
echo.
echo Para ejecutar el servidor:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
echo Accede en: http://localhost:8000
echo Admin en: http://localhost:8000/admin
pause