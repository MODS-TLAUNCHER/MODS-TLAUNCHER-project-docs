#!/usr/bin/env python
import os
import django

# Ajustar esta variable si tu configuración de Django está en otro módulo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biUNestar.settings')
django.setup()

from accounts.models import User
from django.db.models import Count

def limpiar_student_id():
    # 1) Convertir student_id == '' a None
    qs_empty = User.objects.filter(student_id='')
    n_empty = qs_empty.count()
    print(f"Usuarios con student_id '': {n_empty}")
    qs_empty.update(student_id=None)
    print("Cadenas vacías convertidas a NULL.")

    # 2) Buscar duplicados (no-null)
    dups = (
        User.objects
        .values('student_id')
        .annotate(n=Count('id'))
        .filter(n__gt=1, student_id__isnull=False)
    )
    if dups:
        print("student_id duplicados encontrados:")
        for d in dups:
            sid = d['student_id']
            cnt = d['n']
            users = User.objects.filter(student_id=sid)
            print(f"  student_id = {sid}  → {cnt} usuarios")
            for u in users:
                print(f"    - id={u.id}, username={u.username}, email={u.email}")
    else:
        print("No hay student_id duplicados (excluyendo NULL).")

if __name__ == '__main__':
    limpiar_student_id()
    print("Limpieza finalizada.")
