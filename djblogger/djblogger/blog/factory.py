import factory
from factory.faker import faker
from django.contrib.auth.models import User
from .models import Post

# Initialize Faker instance for generating fake data
FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    """
    To generate test posts on database.

    This factory creates Post instances with realistic fake data using the Faker library.
    It's primarily used for testing and populating the database with sample blog posts.

    Parameters
    ----------
    title : str
        Auto-generated fake sentence for post title
    subtitle : str
        Auto-generated fake sentence for post subtitle
    slug : str
        URL-friendly version of the title
    author : User
        Default author object (username: saeed)
    content : str
        Generated multi-paragraph content
    status : str
        Publication status of the post
    tags : list
        Collection of topic tags associated with the post
    """

    class Meta:
        model = Post

    # Define the attributes type according to the post mode
    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    status = "published"

    # Associate posts with a default author named "saeed" or create a new author user.
    author = User.objects.get_or_create(username="saeed")[0]

    @factory.lazy_attribute
    def content(self):
        """
        Generate multi-paragraph content for the blog post.

        Returns
        -------
        str
            Five paragraphs of lorem ipsum-style text, each containing 30 sentences
        """
        data = ""
        for _ in range(0, 5):
            data += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return data

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """
        Add tags to the post after it's generated.

        Parameters
        ----------
        create : bool
            Whether the model instance is being created
        extracted : list, optional
            List of specific tags to add if provided
        **kwargs : dict
            Additional keyword arguments

        Notes
        -----
        If no specific tags are extracted, adds a default set of programming-related tags
        """
        if not create:
            return

        if extracted:
            self.tag.add(extracted)
        else:
            self.tags.add(
                "python",
                "django",
                "javascript",
                "web-development",
                "programming",
                "database",
                "api",
                "front-end",
                "back-end",
                "devpps",
            )
