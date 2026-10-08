# Práctica de Cloud Computing: sitio web con Django y Docker

**Autor:** Diego Corrales  
**Asignatura:** Cloud Computing (clase práctica)

Sitio web de varias páginas hecho con el framework **Django** y ejecutado en contenedores **Docker**. Sigue en tres fases la guía [modeloBaseWeb](https://github.com/evidadeusto/modeloBaseWeb) de eVida: preparar el entorno y la imagen, construir la web y orquestarla con Docker Compose.

## Tecnologías

| Herramienta | Versión | Para qué se usa |
|---|---|---|
| Python | 3.11 (imagen `python:3.11-slim`) | Lenguaje del servidor |
| Django | 5.0 | Framework web: rutas, vistas y plantillas |
| Docker | — | Empaqueta la aplicación y sus dependencias en una imagen |
| Docker Compose | — | Arranca el contenedor con toda su configuración en un solo comando |
| HTML, CSS y JavaScript | — | Diseño de las páginas y menú adaptable a móvil |

## Cómo ejecutarlo

Hace falta tener instalados **Docker Desktop** (en Windows, con WSL 2) y **Git**.

1. Clonar el repositorio y entrar en la carpeta:
   ```bash
   git clone https://github.com/USUARIO/NOMBRE-DEL-REPOSITORIO.git
   cd NOMBRE-DEL-REPOSITORIO
   ```
2. Construir la imagen y arrancar el contenedor:
   ```bash
   docker-compose up --build
   ```
3. En otra terminal, crear la base de datos (solo la primera vez):
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. Opcional, crear un usuario administrador para el panel de Django:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
5. Abrir el sitio en **http://localhost:3000/** y el panel de administración en **http://localhost:3000/admin/**.

Para pararlo: `Ctrl + C` en la terminal y después `docker-compose down`.

## Páginas

| Ruta | Página |
|---|---|
| `/` | Inicio |
| `/plantilla1/` | Plantilla 1 |
| `/plantilla2/` | Plantilla 2 |
| `/plantilla3/` | Plantilla 3 |
| `/plantilla4/` | Plantilla 4 |
| `/admin/` | Panel de administración de Django |

## Fases de la práctica

### Fase 1: estructura básica del proyecto

- Proyecto `proyectoDjango` creado con `django-admin startproject` dentro de un contenedor de Python, sin instalar nada en el ordenador.
- `requirements.txt` con las dependencias (Django 5.0).
- `Dockerfile` basado en `python:3.11-slim` que instala las dependencias y arranca el servidor en el puerto 8000.
- Imagen `imagen_proyecto:v1.0` construida con `docker build`, migraciones de la base de datos y superusuario para el panel de administración.

### Fase 2: aplicación web funcional

- App `web` registrada en `INSTALLED_APPS` de `proyectoDjango/settings.py`.
- Rutas definidas en `web/urls.py` e incluidas desde `proyectoDjango/urls.py`.
- Vistas en `web/views.py`: cada una envía sus datos (`context`) a una plantilla.
- Plantillas con herencia: `base.html` contiene la estructura común e incluye `includes/header.html` y `includes/footer.html`; `home.html` y `plantilla1.html` a `plantilla4.html` la extienden con `{% extends %}` y solo rellenan su contenido.
- Archivos estáticos: `static/css/style.css` con el diseño adaptable a móvil y `static/js/menu.js` con el menú hamburguesa.
- Ruta de las plantillas configurada en `TEMPLATES['DIRS']`.

### Fase 3: Docker Compose

- `docker-compose.yml` con el servicio `web`: imagen `imagen_proyecto:v1.0`, contenedor `contenedor_proyecto`, puertos `3000:8000`, variables de entorno y un volumen que sincroniza el código con el contenedor, de modo que los cambios se ven sin reconstruir la imagen.
- Toda la aplicación se arranca con `docker-compose up` en lugar del comando `docker run` completo.

## Cambio respecto a la guía

El `Dockerfile` añade esta línea antes de `apt-get update`:

```dockerfile
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources
```

En la red donde se hizo la práctica, las descargas de paquetes de Debian por HTTP fallaban (`Connection refused`) y la imagen no se podía construir. La línea hace que esas descargas vayan por HTTPS. En cualquier otra red funciona igual.

## Estructura del proyecto

```
.
├── docker-compose.yml        Servicio web: imagen, contenedor, puertos y volumen
├── Dockerfile                Receta de la imagen de Docker
├── requirements.txt          Dependencias de Python
├── manage.py                 Utilidad de línea de comandos de Django
├── proyectoDjango/           Configuración del proyecto
│   ├── settings.py           Apps instaladas, plantillas, base de datos…
│   └── urls.py               Rutas principales (admin y app web)
└── web/                      App con las páginas del sitio
    ├── urls.py               Rutas de las páginas
    ├── views.py              Vistas: datos que recibe cada página
    ├── templates/
    │   ├── base.html         Estructura común de todas las páginas
    │   ├── home.html
    │   ├── plantilla1.html … plantilla4.html
    │   └── includes/         header.html y footer.html
    └── static/
        ├── css/style.css     Estilos y diseño adaptable
        └── js/menu.js        Menú hamburguesa en móvil
```

La base de datos `db.sqlite3` no se sube al repositorio porque guarda los usuarios creados en local; se genera con el paso 3 de "Cómo ejecutarlo".
