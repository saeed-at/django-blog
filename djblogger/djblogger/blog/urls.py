"""
URL Configuration for the blog application.

This module defines the URL patterns for the blog application, mapping URLs to views.

Attributes
----------
urlpatterns : list
    A list of URL patterns to be matched against incoming requests.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.HomeView.as_view(), name="homepage"),
    # Search page
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    # Single post page
    path("<slug:post>/", views.post_single, name="post_single"),
    # Posts by tag page
    path("tag/<slug:tag>", views.TagListView.as_view(), name="post_by_tag"),
]
