#!/bin/sh

# Author : Mina D
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
python manage.py migrate #optional for Paiza Cloud IDe
