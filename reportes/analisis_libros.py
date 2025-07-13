import os
import sys
sys.path.append("C:/Users/Usuario/Desktop/LIBROTEKA")

import django
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libroteka.settings")
django.setup()

from libros.models import Libro, Autor, Genero, Calificacion

# Configuración visual
sns.set(style="darkgrid")

def promedio_calificaciones_por_genero():
    data = []
    for genero in Genero.objects.all():
        libros = Libro.objects.filter(genero=genero)
        calificaciones = Calificacion.objects.filter(libro__in=libros)
        if calificaciones.exists():
            puntuaciones = [c.puntuacion for c in calificaciones]
            promedio = pd.Series(puntuaciones).mean()
            data.append({'Género': genero.nombre, 'Promedio': promedio})

    df = pd.DataFrame(data)
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Género', y='Promedio')
    plt.title("Promedio de Calificaciones por Género")
    plt.ylabel("Puntaje Promedio")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# 2. Autor más valorado
def promedio_calificaciones_por_autor():
    data = []
    for autor in Autor.objects.all():
        libros = Libro.objects.filter(autor=autor)
        calificaciones = Calificacion.objects.filter(libro__in=libros)
        if calificaciones.exists():
            promedio = pd.Series([c.puntuacion for c in calificaciones]).mean()
            data.append({'Autor': autor.nombre, 'Promedio': promedio})

    df = pd.DataFrame(data)
    plt.figure(figsize=(10,6))
    sns.barplot(data=df.sort_values('Promedio', ascending=False), x='Autor', y='Promedio')
    plt.title("Promedio de Calificaciones por Autor")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# 3. Distribución de calificaciones
def distribucion_calificaciones():
    calificaciones = Calificacion.objects.all()
    puntuaciones = [c.puntuacion for c in calificaciones]
    plt.figure(figsize=(8,6))
    sns.histplot(puntuaciones, kde=True, bins=5)
    plt.title("Distribución de Calificaciones")
    plt.xlabel("Puntuación")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

# 4. Sugerencia de libros por género
def sugerencia_por_genero():
    genero_nombre = input("Ingresá un género exacto (ej: Ciencia Ficción): ")
    try:
        genero = Genero.objects.get(nombre=genero_nombre)
    except:
        print("❌ Género no encontrado.")
        return
    
    libros = Libro.objects.filter(genero=genero)
    data = []
    for libro in libros:
        calificaciones = Calificacion.objects.filter(libro=libro)
        if calificaciones.exists():
            promedio = pd.Series([c.puntuacion for c in calificaciones]).mean()
            cantidad = calificaciones.count()
            data.append({
                'Libro': libro.nombre,
                'Cantidad': cantidad,
                'Promedio': promedio
            })

    df = pd.DataFrame(data)
    if df.empty:
        print("⚠️ No hay libros calificados en este género.")
        return

    df = df.sort_values(['Cantidad', 'Promedio'], ascending=False)
    print("\n📌 Recomendaciones en el género:", genero_nombre)
    print(df)

# Ejecutar funciones
if __name__ == "__main__":
    print("📊 ANALISIS LIBROTEKA")
    promedio_calificaciones_por_genero()
    promedio_calificaciones_por_autor()
    distribucion_calificaciones()
    sugerencia_por_genero()
