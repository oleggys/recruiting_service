from django.template.defaultfilters import register


@register.filter(name='get')
def get_item(dictionary, key):
    return dictionary.get(key)
