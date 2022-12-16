from django import template
from django.template.defaultfilters import slugify
from unidecode import unidecode

register = template.Library()


@register.filter(name='split')
def split(value, splitter):
    return value.split(splitter)


@register.filter(name='slug')
def slug(value):
    return slugify(unidecode(value))
