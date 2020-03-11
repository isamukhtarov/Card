from django.db import models
from django.utils.translation import ugettext_lazy as _
from .options.choices import CARD_STATUS_CHOICE
# Create your models here.


class Card(models.Model):
    seria_numb = models.CharField(_('Seria number'), max_length=255)
    card_number = models.CharField(_('Card number'), max_length=255)
    release_date = models.DateField(_('Card release date'))
    activity_end_date = models.DateField(_('Card activity end date'))
    use_date = models.DateTimeField(_('Card use date'), null=True, blank=True)
    amount = models.FloatField(_('Card amount'), default=0.0)
    status = models.CharField(_('Card status'), choices=CARD_STATUS_CHOICE, default=_('not_activated'), max_length=125)

    def __str__(self):
        return '{}'.format(self.seria_numb)


class PurchaseHistoryInfo(models.Model):
    card = models.ForeignKey(to=Card, verbose_name=_('Purchase History Card'))
    purchase_one_title = models.CharField(_('Purchase one title'), max_length=255)
    purchase_amount = models.FloatField(_('Purchase amount'), default=0.0)
    purchase_date = models.DateTimeField(_('Purchase date'), auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.card.id, self.purchase_one_title)