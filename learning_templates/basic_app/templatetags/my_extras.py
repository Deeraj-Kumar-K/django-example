from django import template

register = template.Library()

@register.filter(name="replace_text")
def cut_text(value,arg):
    """
    This replaces Original text with Current text
    """
    return value.replace(arg,"")

#register.filter('replace_text',cut_text)