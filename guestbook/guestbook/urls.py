"""
Example URLConf for a contact form.

If all you want is the basic ContactForm with default behavior, just
include this URLConf somewhere in your URL hierarchy (for example, at
``/contact/``)>

"""

from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import GuestbookFormView


urlpatterns = patterns('',
                       url(r'^$',
                           GuestbookFormView.as_view(),
                           name='guestbook_form'),
                       url(r'^sent/$',
                           TemplateView.as_view(
                               template_name='guestbook/contact_form_sent.html'
                               ),
                           name='guestbook_form_submitted'),
                       )
