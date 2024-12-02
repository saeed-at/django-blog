import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


# Mark all tests in this module to use the database
pytestmark = pytest.mark.django_db


class TestListbyTag:
    """
    Test suite for tag-based post filtering functionality.

    This class contains tests to verify the behavior of tag-based post listing,
    including URL resolution, HTMX fragment rendering, and tag filtering logic.

    Methods
    -------
    test_tag_url
        Verify the accessibility of tag-filtered post URLs
    test_post_htmx_fragment
        Test HTMX partial template rendering for tagged posts
    test_tag_filter
        Validate correct tag filtering in the response context
    """

    def test_tag_url(self, client, post_factory):
        """
        Test the accessibility and response of tag-filtered post URLs.

        Parameters
        ----------
        client : django.test.Client
            Django test client instance
        post_factory : fixture
            Factory fixture for creating test post objects

        Validates that URLs for tag-filtered posts return successful responses.
        """
        post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client, post_factory):
        """
        Test HTMX partial template rendering for tagged posts.

        Parameters
        ----------
        client : django.test.Client
            Django test client instance
        post_factory : fixture
            Factory fixture for creating test post objects

        Verifies that HTMX requests return the correct partial template.
        """
        post_factory(title="test-post", tags=["test-tag"])

        # Simulate HTMX request by setting custom header
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        response = client.get(url, **headers)

        # Verify the correct template is used for HTMX requests
        assertTemplateUsed(response, "blog/components/post-list-elements-tags.html")

    def test_tag_filter(self, client, post_factory):
        """
        Test tag filtering functionality in the response context.

        Parameters
        ----------
        client : django.test.Client
            Django test client instance
        post_factory : fixture
            Factory fixture for creating test post objects

        Ensures that the correct tag is present in the response context.
        """
        # Create a test post and store it for tag comparison
        post = post_factory(title="test-post", tags=["test-tag"])
        url = reverse("post_by_tag", kwargs={"tag": "test-tag"})
        response = client.get(url)

        # Verify that the tag in the response context matches the post's tag
        assert post.tags.all()[0].slug == response.context["tag"]
