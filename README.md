# Django

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Python][Python]][python-site]
[![Django][Django]][django-site]
[![JavaScript][JavaScript]][javascript-site]
[![Java][Java]][java-site]

#
## OBJETIVOS
Crear Proyecto y Aplicaciones Django 4 dentro de un entorno virtual.

## TEMAS
- Entorno virtual
- Django
- Proyectos
- Aplicaciones
- Modelos
- Migraciones
- Panel de administración

## EJERCICIOS

### Crear Directorio de trabajo
```sh
mkdir myDjangoProjects
```
    
### Crear entorno virtual
```sh
cd myDjangoProjects
virtualenv -p python3 env
```
    
### Activar el Entorno Virtual
```sh
source env/bin/activate
```

### Listamos los paquetes instalados
```sh
pip list
```

### Instalamos Django con pip:
```sh
pip install Django
```
    
### Dentro del entorno virtual. Crear un nuevo proyecto Django
```sh
django-admin startproject myDjangoProject
```

### Crear una aplicación en la raiz y otro dentro de un subdirectorio de aplicaciones
```sh
django-admin startapp myFirstAplication
```
```sh
mkdir myApplications
cd myApplications
django-admin startapp mySecondAplication
```

### Crear un modelo para ```myFirstAplication``` editando su archivo ```models.py```
```sh
vim models.py
```
```sh
from django.db import models
import uuid
# Create your models here.

class Organization(models.Model):    
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    website = models.URLField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, null=False, auto_now=True)
```

### Crear otro modelo para ```mySecondAplication``` editando su archivo ```models.py```
```sh
vim models.py
```
```sh
from django.db import models
import uuid
# Create your models here.

class Menu(models.Model):    
    UBICATION = [
        ('main_menu', 'Main Menu'),
        ('left_sidebar', 'Let Sidebar'),
        ('right_sidebar', 'Right Sidebar'),
        ('tree_menu', 'Tree Menu'),
        ('up_menu', 'Up Menu'),
        ('bottom_menu', 'Bottom Menu'),
    ]
    ubication = models.CharField(null=False, choices=UBICATION, default='main_menu', max_length=20)       
    label = models.CharField(null=False, blank=False, max_length=20)    
    weight = models.IntegerField(null=True, blank=True)    
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    father = models.OneToOneField('self', blank=True, symmetrical=False)

    class Meta:
        ordering = ['ubication', 'label', 'weight', 'status']

    def save(self, *args, **kwargs):
        self.label = self.name.upper()
        return super(Course, self).Menu(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s" % (self.ubication, self.label, self.weight, self.status)
```


-   Registrar el modelo dentro de ```admin.py```
    ```sh
    vim admin.py
    ```
    ```sh
    from django.contrib import admin
    from .models import Video

    # Register your models here.

    admin.site.register(Video)
    ```

-   Añadir la aplicación como una aplicación instalada en el archivo ```Proyecto/settings.py```
    ```sh
    vim settings.py
    ```
    ```sh
    #...
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Apps.Aplicacion1'
    ]
    #...
    ```
-   ```Si estas trabajando en entornos virtuales es muy probable que no reconozca la ruta de la aplicación. Así que debemos editar el archivo apps.py de la aplicación```
    ```sh
    vim apps.py
    ```
    ```sh
    from django.apps import AppConfig


    class Aplicacion1Config(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'Apps.Aplicacion1'
    ```

-   Ingresar al directorio ```.../django_env/Proyecto``` donde se encuentra el archivo ```manage.py``` para realizar la primera migración:
    ```sh
    python manage.py migrate
    ```
    ```sh
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying sessions.0001_initial... OK
    ```
    -   Podemos observar que la base de datos por defecto ```db.sqlite3``` se ha creado con las tablas iniciales
    ```sh
    tree -L 3 ../
    ```
    ```
    ../
    ├── env
    └── Proyecto
        ├── Apps
        │   └── Aplicacion1
        ├── db.sqlite3
        ├── manage.py
        └── Proyecto
            ├── asgi.py
            ├── __init__.py
            ├── __pycache__
            ├── settings.py
            ├── urls.py
            └── wsgi.py
    ```

-   Crear el super usuario para poder ingresar al panel de administración:
    ```sh
    python manage.py createsuperuser
    ```
    ```sh
    Username (leave blank to use 'richart'): richarteq 
    Email address: richarteq@gmail.com
    Password: 
    Password (again): 
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    ```

-   Crear las migraciones. La migración inicial creará el modelo Video.
    ```sh
    python manage.py makemigrations
    ```
    ```sh
    Migrations for 'Aplicacion1':
    Apps/Aplicacion1/migrations/0001_initial.py
        - Create model Video
    ```
-   Realizar una nueva migración para que los cambios se efectuen.
     ```sh
    python manage.py migrate
    ```
    ```sh
    Operations to perform:
    Apply all migrations: Aplicacion1, admin, auth, contenttypes, sessions
    Running migrations:
    Applying Aplicacion1.0001_initial... OK
    ```
-   Ejecutar el servidor
    ```sh
    python manage.py runserver
    ```
    ```sh
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    June 02, 2022 - 14:50:11
    Django version 4.0.5, using settings 'Proyecto.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

-   Acceder al Panel de  administración desde el navegador web a : http://127.0.0.1:8000/admin

    -   Inicio de sesión

        ![DJANGO-PANEL-ADMIN-LOGIN](imagenes/django_admin_01.png)

    -   Portada inicial
        ![DJANGO-PANEL-ADMIN-HOME](imagenes/django_admin_02.png)

    -   Agregando un nuevo video
        ![DJANGO-PANEL-ADMIN-ADD-01](imagenes/django_admin_03.png)

    -   Video agregado satisfactoriamente
        ![DJANGO-PANEL-ADMIN-ADD-02](imagenes/django_admin_04.png)

    -   Ver video
        ![DJANGO-PANEL-ADMIN-VIEW](imagenes/django_admin_05.png)


#

## EJERCICIOS PROPUESTOS
-   Crea un blog sencillo en un entorno virtual utilizando la guía: https://tutorial.djangogirls.org/es/django_start_project/
-   Especificar paso a paso la creación del blog en su informe.
-   Crear un video tutorial donde realice las operaciones CRUD (URL public reproducible online)
-   Adjuntar URL del video en el informe.

#

## CUESTIONARIO
-   ¿Cuál es un estándar de codificación para Python? Ejemplo: Para PHP en el proyecto Pear https://pear.php.net/manual/en/standards.php
-   ¿Qué diferencias existen entre EasyInstall, pip, y PyPM?
-   En un proyecto Django que se debe ignorar para usar git. Vea: https://github.com/django/django/blob/main/.gitignore. ¿Qué otros tipos de archivos se deberían agregar a este archivo?
-   Utilice ```python manage.py shell``` para agregar objetos. ¿Qué archivos se modificaron al agregar más objetos?

#

## REFERENCIAS
-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/
-   https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models
-   https://tutorial.djangogirls.org/es/django_models/
-   https://pear.php.net/manual/en/standards.php
-   https://docs.djangoproject.com/en/4.0/
-   https://www.youtube.com/watch?v=M4NIs4BM1dk
-   https://pypi.org/
-   https://pip.pypa.io/en/latest/user_guide/
-   https://packaging.python.org/en/latest/tutorials/installing-packages/

#

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=flat&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=flat&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/

[Python]: https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat
[python-site]: https://www.python.org/

[Django]: https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=flat
[django-site]: https://www.djangoproject.com/

[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black
[javascript-site]: https://developer.mozilla.org/es/docs/Web/JavaScript/

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Python][Python]][python-site]
[![Django][Django]][django-site]
[![JavaScript][JavaScript]][javascript-site]
[![Java][Java]][java-site]

