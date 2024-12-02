import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    """
    Test suite for the Post model.

    This class contains tests for the Post model's methods and properties.
    """

    def test_str_return(self, post_factory):
        """
        Test the __str__ method of the Post model.

        Parameters
        ----------
        post_factory : function
            A factory function to create Post instances.

        Asserts
        -------
        str
            The string representation of the Post instance matches the title.
        """
        post = post_factory(title="test-post")
        assert post.__str__() == "test-post"

    def test_add_tag(self, post_factory):
        """
        Test adding a tag to a Post instance.

        Parameters
        ----------
        post_factory : function
            A factory function to create Post instances.

        Asserts
        -------
        int
            The number of tags associated with the Post instance is correct.
        """
        x = post_factory(title="test-post", tags=["test-tag"])
        assert x.tags.count() == 1
