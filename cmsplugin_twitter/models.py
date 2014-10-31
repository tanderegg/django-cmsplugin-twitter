from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class TwitterConfig(CMSPlugin):
    """
    Settings for an embeded twitter feed
    """

    number_of_tweets = models.IntegerField(_("Number of Tweets"), default=5)
    username = models.CharField(_("Username"), max_length=255)
    css_class = models.CharField(
        _("Class"), max_length=255, null=True, blank=True
    )

    def __str__(self):
        return _("Tweets from {0}".format(self.username))
