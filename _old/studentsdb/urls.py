"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

import students.views
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    # Students urls
    url(r'^$', students.views.students_list, name='home'),
    url(r'^students/add/$', students.views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.views.students_delete, name='students_delete'),

    # Journal urls
    url(r'^journal/$', students.views.journal, name='journal'),
    url(r'^journal/(?P<gid>\d+)/$', students.views.journal_for_student, name='journal_for_student'),
    url(r'^journal/update/$', students.views.journal_update, name='journal_update'),

    # Groups urls
    url(r'^groups/$', students.views.groups_list, name='groups'),
    url(r'^groups/add/$', students.views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', students.views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', students.views.groups_delete, name='groups_delete'),

    url(r'^admin/', admin.site.urls),
]

if DEBUG:
    pass
# serve files from media folder
#     urlpatterns += patterns('',
#                         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                             'document_root': MEDIA_ROOT}))

# from django.conf.urls import patterns, include, url
# from django.contrib import admin
#
# urlpatterns = patterns('',
#     # Students urls
#     url(r'^$', 'students.views.students_list', name='home'),
#
#     url(r'^admin/', include(admin.site.urls)),
# )
