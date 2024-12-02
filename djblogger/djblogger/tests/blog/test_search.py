import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


pytestmark = pytest.mark.django_db


class TestPostSearch:
    def test_search_url(self, client):
        """Test the search URL returns a 200 status code.

        Parameters
        ----------
        client : django.test.Client
            The test client to simulate requests.
        """
        url = reverse("post_search")
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client, post_factory):
        """Test that the HTMX request returns the correct template.

        Parameters
        ----------
        client : django.test.Client
            The test client to simulate requests.
        post_factory : callable
            A factory to create post instances for testing.
        """
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("post_search")
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements-search.html")

    def test_search_filter(self, client, post_factory):
        """Test that the search filter returns the correct post.

        Parameters
        ----------
        client : django.test.Client
            The test client to simulate requests.
        post_factory : callable
            A factory to create post instances for testing.
        """
        post = post_factory(title="test-post")
        url = reverse("post_search")
        request = f"{url}?q={post.title}"
        response = client.get(request)
        # Assert that the post title is in the first post's title in the response context
        assert post.title in response.context["posts"][0].title
