from django import template

register = template.Library()

@register.simple_tag
def mediapath(image):
    if image:
        return image.url
    return ''