from django.shortcuts import render

from django.http import Http404

from django.http import HttpResponse
from django.template import loader

from .models import Employee

# Create your views here.

def index(request):
    output = Employee.objects.all()
    return HttpResponse(output)

def results(request, a_number):
    response = "You're looking at the results of  %s."
    return HttpResponse(response % a_number)

def temp(request):
    output = Employee.objects.all()
    template = loader.get_template('employees/index.html')
    context = {
        'my_list': output,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def error(request):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception as e:
        raise Http404(e)