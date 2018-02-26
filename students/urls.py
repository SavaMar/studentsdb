from django.conf.urls import url

from students import views

urlpatterns = [
    # url(r'', views.index, name="index"),
    url(r'^', views.students_list, name='home'),
    url(r'^groups/$', views.groups_list, name='groups'),
    url(r'^students/add/$', views.students_add, name='students_add')
]