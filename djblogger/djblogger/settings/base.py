"""
Base settings for the djblogger project.

This module contains the base Django settings that are shared across all environments
(development, production, etc.). It includes core configurations for database, 
installed apps, middleware, templates, and security settings.

Notes
-----
Settings are separated into different files (base.py, dev.py, prod.py) following
the Django split settings pattern for better organization and security.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR points to the directory containing the Django project
BASE_DIR = Path(__file__).resolve().parent.parent


# Security settings loaded from environment variables for better security practices
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG") == "True"

# Define which hosts are allowed to serve this application
ALLOWED_HOSTS = ["*"]  # Note: Should be restricted in production


# Application definition
# List of installed Django apps, including built-in, third-party, and local apps
INSTALLED_APPS = [
    # Django built-in apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "djblogger.blog",
    # Third-party apps
    "django_htmx",  # For HTMX integration
    "taggit",  # For handling post tags
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]


ROOT_URLCONF = "djblogger.urls"


# Template configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # Global templates directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # Custom template tags that should be available globally
            "builtins": [
                "djblogger.blog.templatetags.tag_cloud",
                "djblogger.blog.templatetags.markdown_processing",
            ],
        },
    },
]


WSGI_APPLICATION = "djblogger.wsgi.application"


# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files configuration
STATIC_URL = "statics/"  # URL prefix for static files
STATICFILES_DIRS = [BASE_DIR / "static"]  # Additional static files locations


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Security headers for protection against common web vulnerabilities
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enables XSS filtering in browsers
X_FRAME_OPTIONS = "DENY"  # Prevents clickjacking via iframes
