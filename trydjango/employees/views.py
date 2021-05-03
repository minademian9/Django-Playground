from django.shortcuts import render
from django.http import HttpResponse

from .models import Employee

# Create your views here.

def index(request):
    output = Employee.objects.all()
    return HttpResponse(output)

def results(request, a_number):
    response = "You're looking at the results of  %s."
    return HttpResponse(response % a_number)