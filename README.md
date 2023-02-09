# MU Django

## คำสั่งที่ใช้ใน Django

ติดตั้ง Django (หลังจาก activate env)
`pip install django`

สร้าง Django Project
`django-admin startproject <PROJECT_NAME>`

> `django-admin startproject mysite`

สร้าง Django App
`python manage.py startapp <APP_NAME>`

> `python manage.py startapp blog`

การ makemigration

`python manage.py makemigrations`

การ migrate

`python manage.py migrate`

การสร้าง super user

`python manage.py createsuperuser`

### Setup virtual env

mac os
> python3 -m venv env

windows os
> python -m venv env

### Activate env

mac os
> source /env/bin/activate

windows os
> \env\Script\activate

## Python Shell
* `python manage.py shell`

## Summernote WYSIWYG
* [Summernote](https://github.com/summernote/django-summernote)

Installation
`pip install django-summernote`

## Media (upload file from user)

Require to install pillow library

`pip install pillow`

## Ref Tools
* [vs code](https://code.visualstudio.com/)
* [DB Browser](https://sqlitebrowser.org/)
* [Django web](https://www.djangoproject.com/)