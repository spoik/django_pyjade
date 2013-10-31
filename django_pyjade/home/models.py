from django.db import models
from django.utils.translation import ugettext as _

class Book(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __unicode__(self):
        return u'%s' % self.name
    