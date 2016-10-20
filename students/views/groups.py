# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.

# Views for Groups

def groups_list(request):
    return render(request, 'students/groups.html')


def groups_add(request):
    return HttpResponse('<h1>Group Add form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
