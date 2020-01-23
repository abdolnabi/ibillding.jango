from django import template
from django.template.loader import get_template
register = template.Library()

@register.simple_tag
def define(val=None):
  return val

# @register.simple_tag(takes_context=True)
# def jinja_include(context, filename):
#     template = get_template(filename)
#     return template.render(context.flatten())