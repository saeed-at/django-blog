from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    """
    A model representing a blog post.

    Attributes
    ----------
    title : CharField
        The title of the post.
    subtitle : CharField
        The subtitle of the post.
    slug : SlugField
        A unique slug for the post, used in URLs.
    author : ForeignKey
        The user who authored the post.
    content : TextField
        The main content of the post.
    created_at : DateTimeField
        The date and time when the post was created.
    updated_at : DateTimeField
        The date and time when the post was last updated.
    status : CharField
        The publication status of the post, either 'draft' or 'published'.
    tags : TaggableManager
        Tags associated with the post.
    """

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )  # Status options for the post

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    tags = TaggableManager()

    def get_absolute_url(self):
        """
        Returns the absolute URL for the post to use on template html files to get the urls for redirecting.

        Returns
        -------
        str
            The URL to access the post detail view.
        """
        return reverse("post_single", args=[self.slug])

    class Meta:
        # newest  posts first
        ordering = ("-created_at",)

    def __str__(self):
        """
        Returns a string representation of the post.

        Returns
        -------
        str
            The title of the post.
        """
        return self.title
