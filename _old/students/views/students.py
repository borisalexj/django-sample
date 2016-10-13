# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from ..models import Student
# from students.models import Student


def students_list(request):
#    # return HttpResponse('<h1>Hello World</h1>')
    # template = loader.get_template('students/students_list.html')
    # context = RequestContext(request, {})
#    # return HttpResponse(template.render(context))
    # return render(request, 'students/students_list.html', {})
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/img.jpg'},
        {'id': 2,
         'first_name': u'Олександр',
         'last_name': u'Орєхов',
         'ticket': 852,
         'image': 'img/img.jpg'},
        {'id': 3,
         'first_name': u'Олексій',
         'last_name': u'Борис',
         'ticket': 741,
         'image': 'img/img.jpg'},
    )

    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit students %s</h1>' % (sid,))

def students_delete(request, sid):
    return HttpResponse('<h1>Delete student %s</h1>' % (sid,))