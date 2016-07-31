"""
URLs for the course publisher views.
"""
from django.conf.urls import url

from course_discovery.apps.publisher import views

urlpatterns = [
    url(r'^pre_publisher/(?P<pk>\d+)/$', views.PrePublishView.as_view(), name='pre_publisher'),
]
