import logging
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import ListView, DetailView
from .models import BlogPost


logger = logging.getLogger(__name__)


class IndexView(ListView):

    template_name = 'blog/index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 5


class BlogDetail(DetailView):

    template_name = 'blog/post.html'
    model = BlogPost
