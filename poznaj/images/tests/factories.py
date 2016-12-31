import factory


class ImageFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'image-{}'.format(n))
    image_file = factory.django.ImageField()

    class Meta:
        model = 'images.Image'
