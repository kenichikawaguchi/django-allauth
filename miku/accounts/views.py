import logging

from django.shortcuts import render
from django.views import generic


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = 'account/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_lessons = Lesson.objects.all()
        context['week'] = week
        return context
