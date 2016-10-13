# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Views for groups

def groups_list(request):
    # return HttpResponse('<h1>Groups Listing</h1>')
    return render(request, 'students/groups.html', {})

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit group %s</h1>' % (gid,))

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete group %s</h1>' % (gid,))