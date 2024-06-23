from django import template
import json

register = template.Library()


@register.filter
def load_json(value):
    try:
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return value


@register.filter(name='get_item')
def get_item(dictionary, key):
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter
def calculate_percentage(option_votes, total_votes):
    if total_votes > 0:
        return round((option_votes / total_votes) * 100, 1)
    else:
        return 0