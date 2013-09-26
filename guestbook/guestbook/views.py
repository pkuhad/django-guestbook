"""
View which can render and send email from a contact form.

"""

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.http import HttpResponse

from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from .forms import GuestbookForm
from .models import GuestBook

class GuestbookFormView(FormView):
    form_class = GuestbookForm
    template_name = 'guestbook/contact_form.html'
    model = GuestBook
    
    def get_context_data(self, **kwargs):
        kwargs['guest_posts'] = self.model.objects.all()
        return kwargs

    def form_valid(self, form):
        return HttpResponse("ok fine")
