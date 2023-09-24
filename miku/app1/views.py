import logging
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

from django.shortcuts import render, redirect

from django.core.mail import EmailMessage
from django.conf import settings

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('app1:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Message was sent.')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


def contact_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            initial_values = {"name": request.user.username, "email": request.user.email, "title": "", "message": ""}
            form = InquiryForm(initial_values)
        else:
            form = InquiryForm()
        return render(request, "inquiry.html", {'form': form})
    else:
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            if request.user.is_authenticated:
                message = "Member's Message:\n" + message
            else:
                message = "Guest's Message:\n" + message

            subject = "Inquiry: {}".format(title)

            message = \
                'Sender:{0}\nEmail: {1}\nTitle:{2}\nMessage:\n{3}'\
                .format(name, email, title, message)

            EMAIL_ADMIN = getattr(settings, "EMAIL_ADMIN", None)
            from_email = EMAIL_ADMIN
            to_list = [
                email
            ]
            cc_list = [
                EMAIL_ADMIN
            ]
            bcc_list = [
            ]
            message = EmailMessage(subject=subject, body=message, from_email=from_email,
                                     to=to_list, cc=cc_list, bcc=bcc_list)
            message.send()
            messages.success(
                request, 'Inquiry was sent correctly.')
            return redirect('app1:index')

