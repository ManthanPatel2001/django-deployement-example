from unicodedata import name
from django import template

register = template.Library()

@register.filter(name='cutting')
def cut(val,arg):
    """
    This function cut all the value from arg
    """
    return val.replace(arg,' ')


# register.filter('cutting', cut)