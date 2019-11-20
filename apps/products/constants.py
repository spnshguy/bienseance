from django.utils.translation import ugettext_lazy as _

ASCENDING, DESCENDING, POPULAR = range(3)

FILTER_CHOICES = (
    (None, 'Filtre'),
    (ASCENDING, _('Ascendant')),
    (DESCENDING, _('Descendant')),
    (POPULAR, _('Populaire'))
)
