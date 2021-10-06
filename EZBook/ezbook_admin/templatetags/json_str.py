from django.utils.safestring import mark_safe
from django.template import Library
from django.core import serializers


register = Library()


@register.filter(is_safe=True)
def json_str(obj):
    data = serializers.serialize('json', [obj])
    return mark_safe(data)
