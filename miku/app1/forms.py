from django import forms
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.translation import gettext as _


class InquiryForm(forms.Form):
    name = forms.CharField(label=_("name"), max_length=30)
    email = forms.EmailField(label=_("email"))
    title = forms.CharField(label=_("title"), max_length=30)
    message = forms.CharField(label=_("message"), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'name'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'email'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'title'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'message'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'Inquiry {}'.format(title)
        message = 'Sender: {0}\nEmail: {1}\nMessage:\n{2}'.format(name, email, message)
        EMAIL_ADMIN = getattr(settings, "EMAIL_ADMIN", None)
        from_email = EMAIL_ADMIN
        to_list = [
            email
        ]
        cc_list = [
        ]
        bcc_list = [
            EMAIL_ADMIN
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list, bcc=bcc_list)
        message.send()

