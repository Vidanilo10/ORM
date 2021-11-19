from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

'''
def student_list_(request) -> HttpResponse:
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

'''

'''
def student_list_(request):
    posts = Student.objects.filter(firstname__startswith='Dan') | Student.objects.filter(surname__startswith='baldwin')
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

'''

'''
def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})
'''

'''
def student_list_(request):
    posts = Student.objects.filter(Q(firstname__startswith='Victor') & Q(classroom=701))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})
'''

'''
def student_list_(request):
    posts = Student.objects.filter(~Q(firstname__startswith='Victor') & ~Q(classroom=701))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})
'''


def student_list_(request):
    posts = Student.objects.filter(classroom=701).only('firstname', 'age')
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})
