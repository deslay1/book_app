from django import template

register = template.Library()


@register.filter(name='calculate_diff')
def calculate_diff(value, arg):
    return value-int(arg)
