import markdown as md  # Import the markdown library for processing markdown text
from django import template  # Import Django's template module
from django.template.defaultfilters import stringfilter

# Register the template filter with Django
register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """
    Convert a string of markdown text to HTML.

    Parameters
    ----------
    value : str
        A string containing markdown formatted text.

    Returns
    -------
    str
        A string containing the HTML representation of the markdown input.
    """
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])
