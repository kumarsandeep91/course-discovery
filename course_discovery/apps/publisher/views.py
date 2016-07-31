"""
Course publisher views.
"""
from django.views.generic import detail
from course_discovery.apps.publisher.models import CourseRun
from course_discovery.apps.publisher.wrappers import CourseRunWrapper


class PrePublishView(detail.DetailView):
    """ Pre Publish View."""
    model = CourseRun
    template_name = 'publisher/pre_publish/home.html'

    def get_context_data(self, **kwargs):
        context = super(PrePublishView, self).get_context_data(**kwargs)
        context['object'] = CourseRunWrapper(context['object'])
        return context
