from django import template
register = template.Library()

@register.filter
def getLen(lis):
    return len(lis)