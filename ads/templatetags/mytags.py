from django import template


register = template.Library()


@register.filter
def get_create_time(data):
    return data.strftime('%Y-%m-%dT%H:%M:%S+03:00')

