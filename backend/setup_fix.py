"""
Script para crear la estructura de carpetas correcta
Ejecutar: python setup_fix.py
"""
import os
import sys

# Estructura de carpetas
structure = {
    '': ['manage.py', 'requirements.txt', '.env', 'setup_fix.py'],
    'biUNestar': ['__init__.py', 'settings.py', 'urls.py', 'wsgi.py', 'asgi.py'],
    'accounts': ['__init__.py', 'apps.py', 'models.py', 'forms.py', 'views.py', 'urls.py', 'admin.py'],
    'habits': ['__init__.py', 'apps.py', 'models.py', 'forms.py', 'views.py', 'urls.py', 'admin.py'],
    'resources': ['__init__.py', 'apps.py', 'models.py', 'forms.py', 'views.py', 'urls.py', 'admin.py'],
    'static/css': ['custom.css'],
    'static/js': ['custom.js'],
    'templates/accounts': ['login.html', 'register.html'],
    'templates/habits': ['dashboard.html', 'habit_form.html'],
}

# Contenido de los archivos
file_contents = {
    'manage.py': '''#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biUNestar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()''',
    
    'requirements.txt': '''Django==4.2
psycopg2-binary==2.9.7
Pillow==10.1.0
django-crispy-forms==2.0
crispy-bootstrap5==0.7''',
    
    '.env': '''DEBUG=True
SECRET_KEY=django-insecure-biunestar-dev-key-2024''',
    
    'biUNestar/settings.py': '''import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-biunestar-dev-key-2024')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'accounts',
    'habits',
    'resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biUNestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'biUNestar.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField''',
    
    'biUNestar/urls.py': '''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('habits.urls')),
    path('accounts/', include('accounts.urls')),
    path('resources/', include('resources.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)''',
    
    'biUNestar/wsgi.py': '''import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biUNestar.settings')
application = get_wsgi_application()''',
    
    'biUNestar/asgi.py': '''import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biUNestar.settings')
application = get_asgi_application()''',
    
    'accounts/__init__.py': '',
    'accounts/apps.py': '''from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Gestión de Usuarios''',
    
    'accounts/models.py': '''from django.contrib.auth.models import AbstractUser
from django.db import models
import hashlib
import os

class User(AbstractUser):
    institutional_email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)
    career = models.CharField(max_length=100)
    semester = models.IntegerField(default=1)
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    password_salt = models.CharField(max_length=64, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.password_salt:
            self.password_salt = hashlib.sha256(os.urandom(60)).hexdigest()
        super().save(*args, **kwargs)
    
    def set_password(self, raw_password):
        if not self.password_salt:
            self.password_salt = hashlib.sha256(os.urandom(60)).hexdigest()
        salted_password = f"{raw_password}{self.password_salt}"
        super().set_password(salted_password)
    
    def check_password(self, raw_password):
        salted_password = f"{raw_password}{self.password_salt}"
        return super().check_password(salted_password)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-date_joined']''',
    
    'accounts/forms.py': '''from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
                 'institutional_email', 'student_id', 'career', 'semester',
                 'password1', 'password2']''',
    
    'accounts/views.py': '''from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from .models import User

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, '¡Registro exitoso!')
        return redirect(self.success_url)

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')''',
    
    'accounts/urls.py': '''from django.urls import path
from .views import RegisterView, profile_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
]''',
    
    'accounts/admin.py': '''from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'institutional_email', 'student_id', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'institutional_email', 'student_id')''',
}

# Crear estructura
print("Creando estructura de carpetas...")
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        filepath = os.path.join(folder, file)
        
        # Si es archivo __init__.py vacío
        if file == '__init__.py':
            if not os.path.exists(filepath):
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('')
            continue
        
        # Si el archivo ya existe, no sobreescribir
        if os.path.exists(filepath):
            print(f"✓ {filepath} ya existe")
            continue
        
        # Crear archivo con contenido si existe
        if filepath in file_contents or file in file_contents:
            content_key = filepath if filepath in file_contents else file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(file_contents[content_key])
            print(f"✓ Creado: {filepath}")
        else:
            # Crear archivo vacío
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('')
            print(f"✓ Creado (vacío): {filepath}")

print("\n✅ Estructura creada correctamente!")
print("\nAhora ejecuta estos comandos:")
print("1. venv\\Scripts\\activate")
print("2. pip install -r requirements.txt")
print("3. python manage.py makemigrations")
print("4. python manage.py migrate")
print("5. python manage.py createsuperuser")
print("6. python manage.py runserver")