from django import template
import json

register = template.Library()


@register.filter
def load_json(value):
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return value
