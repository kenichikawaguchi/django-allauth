import logging
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic

from django.conf import settings
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.models import EmailAddress


logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "emailaddresses": list(
                    EmailAddress.objects.filter(user=self.request.user).order_by(
                        "email"
                    )
                )
            }
        )
        return context
