from django import template

register = template.Library()


@register.filter
def get_at_index(object_list, index):
    return object_list[index]


@register.filter
def get_by_key(dict_obj, key):
    return dict_obj.get(key)


@register.filter
def get_filename(filename):
    return str(filename)[9:]
