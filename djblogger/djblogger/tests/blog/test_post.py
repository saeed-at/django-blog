import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestPostSingle:
    def test_post_single_url(self, client, post_factory):
        """
        Test the URL for a single blog post.

        This test checks that the URL for a single blog post returns a
        successful response (HTTP 200) when accessed with a valid post slug.

        Parameters
        ----------
        client : django.test.Client
            The test client used to simulate requests to the application.
        post_factory : callable
            A factory function to create a post instance for testing.
        """
        post = post_factory()

        # Generate the URL for the single post using its slug
        url = reverse("post_single", kwargs={"post": post.slug})
        response = client.get(url)

        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200
