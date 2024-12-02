import factory
from django.contrib.auth.models import User
from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating User model instances for testing.

    Parameters
    ----------
    password : str
        User password, defaults to "test"
    username : str
        User login name, defaults to "test"
    is_superuser : bool
        Flag for superuser status, defaults to True
    is_staff : bool
        Flag for staff status, defaults to True

    Notes
    -----
    Uses factory.django.DjangoModelFactory to automate test data creation
    for Django's built-in User model.
    """

    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating blog Post model instances for testing.

    Parameters
    ----------
    title : str
        Post title, defaults to "x"
    subtitle : str
        Post subtitle, defaults to "x"
    slug : str
        URL slug for the post, defaults to "x"
    author : UserFactory
        Foreign key to User model, auto-created via UserFactory
    content : str
        Main content of the post, defaults to "x"
    status : str
        Publication status, defaults to "published"
    tags : list, optional
        List of tags to associate with the post

    Notes
    -----
    Uses factory.django.DjangoModelFactory to automate test data creation
    for the custom Post model.
    """

    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    # Create a related User instance automatically
    author = factory.SubFactory(UserFactory)

    content = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """
        Handles many-to-many relationship for tags after post creation.

        Parameters
        ----------
        create : bool
            Whether the model instance is being created
        extracted : list
            List of tags to be added to the post
        **kwargs : dict
            Additional keyword arguments

        Notes
        -----
        This method is automatically called after the post instance is created
        to handle the many-to-many relationship with tags.
        """
        if not create:
            return
        if extracted:
            self.tags.add(*extracted)
