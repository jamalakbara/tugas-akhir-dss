from django import template
register = template.Library()

@register.filter
def indexList(lis):
    adaw = list()
    for i, item in enumerate(lis):
        adaw.append([i+1, item])
    return adaw