from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<int:a_number>', views.results, name='result'),
    path('temp/', views.temp, name='template'),
    path('error/', views.error, name='error 404 page'),

]