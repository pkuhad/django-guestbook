from django.db import models
from django.utils.translation import ugettext as _

class GuestBook(models.Model):
    
    message = models.TextField(verbose_name=_(u'Message'), blank=True)
    name = models.CharField(max_length=150, verbose_name=_(u'Name'))
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return 'Message by %s' % self.name


