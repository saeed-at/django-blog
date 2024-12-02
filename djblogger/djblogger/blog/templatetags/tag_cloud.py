from django import template
from taggit.models import Tag

# Register the template library for custom template tags
register = template.Library()


@register.inclusion_tag("blog/components/tag-cloud.html")
def sidebar_tag_cloud():
    """Generate data for rendering a tag cloud in the sidebar.

    This template tag fetches all available tags from the database
    to create a tag cloud visualization.

    Returns
    -------
    dict
        A dictionary containing:
        dn_tags : QuerySet
            All Tag objects from the database

    """

    db_tags = Tag.objects.all()

    # Return tags in a dictionary to be used as template context
    return {"tags": db_tags}
