import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):  #! where dose post_factory come from
        #! what happen when this run
        post = post_factory(title="test-post")
        assert post.__str__() == "test-post"
