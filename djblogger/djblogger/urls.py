"""
Main URL Configuration for djblogger project.

This module handles the root URL configurations and includes other URL patterns
from different apps within the project.

Notes
-----
The urlpatterns list routes URLs to views using Django's URL dispatcher.
For more details, see: https://docs.djangoproject.com/en/4.2/topics/http/urls/

See Also
--------
django.urls.path : Function to define URL patterns
django.urls.include : Function to include other URLconf modules
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # This allows the blog app to handle its own URL routing independently
    path("", include("djblogger.blog.urls")),
]
