import factory
from poznaj.points.tests.factories import PointFactory
from poznaj.stories.tests.factories import StoryFactory


class ImageFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'image-{}'.format(n))
    image_file = factory.django.ImageField()
    copyright = factory.LazyAttribute(lambda c: 'CC0')
    story = factory.SubFactory(StoryFactory)
    point = factory.SubFactory(PointFactory)

    class Meta:
        model = 'images.Image'
