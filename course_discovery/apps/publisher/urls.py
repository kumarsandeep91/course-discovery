"""
URLs for the course builder views.
"""
from django.conf.urls import url
from course_discovery.apps.publisher.views import CourseListing

urlpatterns = [
    url(r'^listing/$', CourseListing.as_view(), name='courses_list'),
]