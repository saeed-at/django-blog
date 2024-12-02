import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

# Mark all tests in this module to use the Django database
pytestmark = pytest.mark.django_db


class TestHomePage:
    """
    Test suite for the homepage view.
    """

    def test_homepage_url(self, client):
        """
        Test that the homepage URL returns a 200 status code.

        Parameters
        ----------
        client : django.test.Client
            The test client used to simulate requests to the application.
        """
        url = reverse("homepage")
        response = client.get(url)
        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client):
        """
        Test that an HTMX request to the homepage returns the correct template.

        Parameters
        ----------
        client : django.test.Client
            The test client used to simulate requests to the application.
        """
        # Headers to simulate an HTMX request
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("homepage")
        response = client.get(url, **headers)
        # Assert that the response uses the specified template
        assertTemplateUsed(response, "blog/components/post-list-elements.html")
