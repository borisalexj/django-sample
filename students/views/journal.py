# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


# Create your views here.


# Views for Journal

def journal(request):
    return render(request, 'students/journal.html')

