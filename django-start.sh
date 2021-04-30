#!/bin/sh

# Author : Mina D
django-admin startproject myproject
python myproject/manage.py startapp myapp
python manage.py migrate 
