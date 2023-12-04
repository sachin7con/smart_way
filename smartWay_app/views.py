from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Student

# Create your views here.
def home(request):
    return HttpResponse("Jay Shree GAneshay Namah")


def students(request):
    myStudent = Student.objects.all().values()
    template = loader.get_template('students.html')
    context = {
        'myStudent': myStudent,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mystudent = Student.objects.all().get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))
