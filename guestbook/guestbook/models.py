from django.db import models
from django.utils.translation import ugettext as _

class Newsletter(models.Model):
    
    message = models.TextField(verbose_name=_(u'Message'), blank=True)
    name = models.CharField(max_length=150, verbose_name=_(u'Name'))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Message by %s' % self.name


