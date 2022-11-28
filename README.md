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
Crear un Proyecto y Aplicaciones Django 4 dentro de un entorno virtual.

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
    
### Ingresar al directorio de trabajo
```sh
cd myDjangoProjects
```

### Crear entorno virtual
```sh
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

### Crear una aplicación en la raiz
```sh
django-admin startapp myFirstAplication
```

### Crear un subdirectorio para albergar varias aplicaciones
```sh
mkdir myApplications
```

### Ingresar al subdirectorio de aplicaciones
```sh
cd myApplications
```

### Crear una aplicación dentro del subdirectorio de aplicaciones
```sh
django-admin startapp mySecondAplication
```

### Crear un modelo para ```myFirstAplication``` editando el archivo ```myFirstAplication/models.py```
```sh
vim models.py
```
```sh
from django.db import models

# Create your models here.

class Organization(models.Model):    
    name = models.CharField(unique=True, max_length=150, null=False, blank=False)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    website = models.URLField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, null=False, auto_now=True)
```

### Crear otro modelo para ```mySecondAplication``` editando el archivo ```mySecondAplication/models.py```
```sh
vim models.py
```
```sh
from django.db import models

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


### Registrar los modelos dentro de los archivos ```admin.py``` correspondientes
```sh
vim admin.py
```
```sh
from django.contrib import admin

# Register your models here.

from .models import Organization
admin.site.register(Organization)
```
```sh
from django.contrib import admin

# Register your models here.

from .models import Menu
admin.site.register(Menu)
```

### Instalar las aplicaciones en el archivo ```myDjangoProject/settings.py```
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
    'myFirstAplication',
    'myAplications.mySecondAplication',
]
#...
```

### Configure apps.py de la aplicación mySecondAplication
```sh
vim apps.py
```
```sh
from django.apps import AppConfig


class MysecondaplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myAplications.mySecondAplication'
```

### Realice la primera migración, ubicandose donde se encuentra el archivo ```manage.py```
```sh
python3 manage.py migrate
```

### Crear el super usuario para poder ingresar al panel de administración:
```sh
python3 manage.py createsuperuser
```
    
### Crear las migraciones. La migración inicial creará los modelos.
```sh
python3 manage.py makemigrations
```
    
### Ejecutar el servidor
```sh
python3 manage.py runserver
```

### Acceda al Proyecto o al Panel de  administración
```sh
http://127.0.0.1:8000/
```
```sh
http://127.0.0.1:8000/admin/
```

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
