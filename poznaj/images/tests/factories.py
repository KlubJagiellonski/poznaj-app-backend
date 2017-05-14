import factory


class ImageFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'image-{}'.format(n))
    image_file = factory.django.ImageField()
    copyright = factory.LazyAttribute(lambda c: 'CC0')

    class Meta:
        model = 'images.Image'
