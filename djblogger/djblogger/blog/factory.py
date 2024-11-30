import factory
from factory.faker import faker
from django.contrib.auth.models import User
from .models import Post


FAKE = faker.Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    subtitle = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")

    author = User.objects.get_or_create(username="saeed")[0]

    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(0, 5):
            x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return x

    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:  # if no tage is choosen, then leave it
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
