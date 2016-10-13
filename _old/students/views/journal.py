# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Views for journal
def journal(request):
    # return HttpResponse('<h1>Journal</h1>')
    return render(request, 'students/journal.html', {})

def journal_for_student(request, sid):
    return HttpResponse('<h1>Journal for student %s</h1>' % (sid,))

def journal_update(request):
    return HttpResponse('<h1>Journal Update</h1>')