from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from libs import mailchimp
from libs.mailchimp.chimpy.chimpy import ChimpyException


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Nom'), max_length=100,
                           widget=forms.TextInput(attrs={'class': 'textinput textInput form-control'}))
    email = forms.EmailField(label=_('Courriel'), widget=forms.EmailInput(attrs={'class': 'emailinput form-control'}))
    message = forms.CharField(label=_('Message'), widget=forms.Textarea(attrs={'class': 'textarea form-control'}))


class NewsletterForm(forms.Form):
    email = forms.EmailField(label=_('Courriel'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            list = mailchimp.utils.get_connection().get_list_by_id(settings.MAILCHIMP_SUBSCRIBE_LIST_ID)
            list.subscribe(email, {'EMAIL': email})
        except ChimpyException as e:
            raise ValidationError(_('Une erreur est survenue lors du traitement de votre demande.'))
        return email
