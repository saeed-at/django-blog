"""
Test configuration module for pytest fixtures and factory registration.

This module serves as a central configuration point for pytest, specifically
handling the registration of factory boy factories for testing.

Notes
-----
conftest.py is a special pytest file that is automatically discovered and
can define fixtures available to all test files in the same directory and
its subdirectories.
"""

from pytest_factoryboy import register
from .factories import PostFactory


register(PostFactory)
