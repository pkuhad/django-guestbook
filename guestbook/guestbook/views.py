"""
View which can render and send email from a contact form.

"""

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse

from .forms import GuestbookForm


class GuestbookFormView(FormView):
    form_class = GuestbookForm
    template_name = 'guestbook/contact_form.html'

    def form_valid(self, form):
        return HttpResponse("ok fine")
