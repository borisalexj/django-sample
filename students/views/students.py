# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.

# Views for Students
from ..models import Student


def students_list(request):
    # raise Http404
    # return HttpResponse('<h1>Hello World</h1>')
    # students = (
    #     {'id': 1,
    #      'first_name': u'John',
    #      'last_name': u'Connor',
    #      'ticket': 333,
    #      'image': 'img/default.jpg'
    #      },
    #     {'id': 2,
    #      'first_name': u'Arnold',
    #      'last_name': u'Shwarcenegger',
    #      'ticket': 555,
    #      'image': 'img/default.jpg'
    #      },
    #     {'id': 3,
    #      'first_name': u'Александр',
    #      'last_name': u'Орєхов',
    #      'ticket': 777,
    #      'image': 'img/default.jpg'
    #      },
    # )
    students = Student.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students.reverse()

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

