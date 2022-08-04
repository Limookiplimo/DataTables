from multiprocessing import context
from django.shortcuts import render
from HR.models import Employee

# Create your views here.


def home(request):
    employee_list = Employee.objects.all()
    context = {'employees': employee_list}
    return render(request, 'home.html', context)
