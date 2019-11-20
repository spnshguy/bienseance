from cms.templatetags.cms_tags import Placeholder, PlaceholderOptions
from django import template
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe
from classytags.arguments import Argument, MultiValueArgument

from apps.front.forms import ContactForm, NewsletterForm

__author__ = 'chris'

register = template.Library()


@register.simple_tag
def include_static(path, encoding='UTF-8'):
    file_path = finders.find(path)
    with open(file_path, "r", encoding=encoding) as f:
        string = f.read()
        return string


@register.tag
class RenderPlaceholder(Placeholder):
    """
    Render the content of a placeholder to a variable.

    {% placeholder "placeholder_name" as variable_name %}
    """
    name = "get_placeholder"

    options = PlaceholderOptions(
        Argument('name', resolve=False),
        MultiValueArgument('extra_bits', required=False, resolve=False),
        'as',
        Argument('varname', resolve=False),
        blocks=[
            ('endplaceholder', 'nodelist'),
        ],
    )

    def render_tag(self, context, name, extra_bits, varname, nodelist=None):
        content = super(RenderPlaceholder, self).render_tag(context, name, extra_bits, nodelist)
        context[varname] = mark_safe(content)
        return ""


@register.inclusion_tag('_contact_form.html')
def contact_form():
    contact_form = ContactForm(prefix='contact')
    return dict(contact_form=contact_form)


@register.inclusion_tag('_newsletter_form.html')
def newsletter_form():
    newsletter_form = NewsletterForm(prefix='newsletter')
    return dict(newsletter_form=newsletter_form)
