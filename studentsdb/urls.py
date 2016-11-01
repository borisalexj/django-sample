"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import django
from django.conf.urls import url, patterns
from django.contrib import admin
import students.views
from studentsdb.StudentsList import StudentList

urlpatterns = [
    # Students urls
    url(r'^$', students.views.students_list, name='home'),
    url(r'^students/add/$', students.views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.views.students_delete, name='students_delete'),

    url(r'^student_list/$', StudentList.as_view()),

    # Journal urls
    url(r'^journal/$', students.views.journal, name='journal'),
    url(r'^journal/(?P<sid>\d+)/$', students.views.journal_for_student, name='journal_for_student'),

    # Groups urls
    url(r'^groups/$', students.views.groups_list, name='groups'),
    url(r'^groups/add/$', students.views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', students.views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', students.views.groups_delete, name='groups_delete'),

    url(r'^contact-admin/$', 'students.views.contact_admin', name='contact_admin'),

    url(r'^admin/', admin.site.urls),

    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]

from .settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static

if DEBUG:
# serve files from media folder
    urlpatterns += urlpatterns + [url(r'^media/(?P<path>.*)$',  django.views.static.serve, {'document_root': MEDIA_ROOT}),]
    # urlpatterns += urlpatterns + static((r'^media/(?P<path>.*)$', {'document_root': MEDIA_ROOT}), document_root = MEDIA_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
