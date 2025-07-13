
# LIBROTEKA 📚

Proyecto completo desarrollado con Django, enfocado en la gestión visual e interactiva de libros. Ofrece autenticación, carga de libros en PDF, calificación, recomendaciones por género y visualización de datos mediante gráficos 📊.

---

## 🛠 Instalación del Proyecto

```bash
git clone https://github.com/Edgarchooo/LIBROTEKA.git
cd LIBROTEKA
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 Autenticación y Registro de Usuario

| Acción | Captura |
|-------|---------|
| Home sin autenticar | ![](captures/home_no_autenticado.jpg) |
| Formulario de login | ![](captures/formulario_login.jpg) |
| Home autenticado | ![](captures/home_autenticado.jpg) |

---

## 📥 Subida y Edición de Libros

| Acción | Captura |
|-------|---------|
| Subir nuevo libro | ![](captures/subir_libro_web.jpg) |
| Confirmación de libro subido | ![](captures/confirmacion_subida_libro.jpg) |
| Edición desde admin | ![](captures/admin_edicion_libro.jpg) |

---

## 🌟 Calificaciones

| Acción | Captura |
|-------|---------|
| Formulario para calificar libro | ![](captures/formulario_calificacion.jpg) |
| Promedio por género: Este gráfico muestra el promedio de calificaciones que recibió cada género literario. Es útil para identificar qué tipo de libros son mejor valorados por los usuarios de la plataforma.  | ![](captures/grafico_promedio_genero.jpg.jpg) |
| Promedio por autor: Este gráfico representa el promedio de puntuación obtenida por cada autor en base a las calificaciones recibidas por sus libros. Permite visualizar qué autores son más populares o mejor valorados. | ![](captures/grafico_promedio_autor.jpg) |
| Distribución de calificaciones: Este gráfico ilustra la distribución total de calificaciones en la plataforma. Ayuda a observar la tendencia general de las puntuaciones dadas, por ejemplo, si los usuarios tienden a calificar con valores altos o bajos. | ![](captures/grafico_distribucion.jpg) |

---

## 🧠 Recomendaciones por Género

| Acción | Captura |
|-------|---------|
| Vista inicial | ![](captures/recomendacion_genero.jpg) |
| Resultados | ![](captures/resultados_recomendaciones.jpg) |

---

## 📋 Visualización y API

| Acción | Captura |
|-------|---------|
| Ver libros web | ![](captures/lista_libros_web.jpg) |
| Ver libros en Postman | ![](captures/listar_libros_postman.jpg) |
| Crear libro en Postman | ![](captures/crear_libro_postman.jpg) |
| Token login Postman | ![](captures/login_postman.jpg) |
| Libro no encontrado | ![](captures/libro_no_encontrado.jpg) |

---

## 🔧 Panel de Administración

| Acción | Captura |
|-------|---------|
| Modelos visibles | ![](captures/panel_admin_modelos.jpg) |

---

© 2025 LIBROTEKA - Proyecto Django Visual
