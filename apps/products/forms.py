from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from apps.products.constants import FILTER_CHOICES
from apps.products.models import Product, Designer, Tag, Magazine


class ProductAdminForm(forms.ModelForm):
    model = Product
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['product_images'].required = False
        self.fields['tags'].required = False


class MagazineAdminForm(forms.ModelForm):
    model = Magazine
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MagazineAdminForm, self).__init__(*args, **kwargs)


class ProductFilterForm(forms.Form):
    order = forms.ChoiceField(label='', choices=FILTER_CHOICES, required=False)
    designer = forms.ModelChoiceField(queryset=Designer.objects.all(), label='', empty_label=_('Designer'))
    tag = forms.ModelChoiceField(label='', queryset=Tag.objects.all(), empty_label=_('Valeurs'))


class MagazineFilterForm(forms.Form):
    order = forms.ChoiceField(label='', choices=FILTER_CHOICES, required=False)


class ProductOrderingForm(forms.ModelForm):
    amount = forms.IntegerField(label='', initial=1)
    available_sizes = forms.ModelChoiceField(label='', queryset=None, required=False, empty_label=None)

    class Meta:
        model = Product
        fields = 'id',

    def __init__(self, *args, **kwargs):
        super(ProductOrderingForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance, 'available_sizes'):
            self.fields['available_sizes'].queryset = self.instance.available_sizes.all().order_by('id')
        attributes = {'min': 1}
        if hasattr(self.instance, 'current_stock'):
            attributes.update({'max': self.instance.current_stock, })
        self.fields['amount'].widget = forms.NumberInput(attrs=attributes)

    def clean_amount(self):
        size = self.cleaned_data.get('amount')
        if not size:
            raise ValidationError(_('Please select an amount'))
        if int(size) <= 0:
            raise ValidationError(_('Please select a proper amount'))
        return size
