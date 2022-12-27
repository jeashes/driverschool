from django import template
from django.template.defaultfilters import slugify
from unidecode import unidecode
from school.models import *
from school import models

register = template.Library()


@register.filter(name='split')
def split(value, splitter):
    return value.split(splitter)


@register.filter(name='slug')
def slug(value):
    return slugify(unidecode(value))


@register.filter(name='get_cities_for_area')
def get_cities_for_area(value):
    return models.City.objects.filter(area__name=value)


@register.filter(name='get_cities_for_letter')
def get_cities_for_letter(value):
    return models.City.objects.filter(name__startswith=value)
