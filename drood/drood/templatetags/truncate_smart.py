# From http://djangosnippets.org/snippets/1259/

from django import template

register = template.Library()


@register.filter
def truncate_smart(value, limit=90):
    if len(value) > limit:
        # Limits the number of characters in value to max_length (blunt cut)
        truncated_val = value[:limit]
        # Check if the next upcoming character after the limit is not a space,
        # in which case it might be a word continuing
        if value[limit] != " ":
            # rfind will return the last index where matching the searched character,
            # in this case we are looking for the last space
            # Then we only return the number of character up to that last space
            truncated_val = truncated_val[:truncated_val.rfind(" ")]

        #if the last char is a comma, get rid of it
        if truncated_val.endswith(','):
            truncated_val = truncated_val[:-1]

        return '%s...' % truncated_val

    return value


@register.filter
def truncate_complementary(value, limit=90):
    truncated_val = truncate_smart(value, limit)

    return value.replace(truncated_val, '')
