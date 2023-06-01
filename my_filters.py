from django import template

register = template.Library()


@register.filter
def extract_airport_code(value):
    if not value:
        return ''
    return value.split('(')[-1].strip(')')
