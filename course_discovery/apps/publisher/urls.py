"""
URLs for the course publisher views.
"""
from django.conf.urls import url

from course_discovery.apps.publisher import views

urlpatterns = [
    url(r'^courses/new$', views.CreateCourseView.as_view(), name='publisher_courses_new'),
    url(r'^courses/(?P<pk>\d+)/edit/$', views.UpdateCourseView.as_view(), name='publisher_courses_edit'),
    url(r'^course_runs/new$', views.CreateCourseRunView.as_view(), name='publisher_course_runs_new'),
    url(r'^course_runs/(?P<pk>\d+)/edit/$', views.UpdateCourseRunView.as_view(), name='publisher_course_runs_edit'),

]
