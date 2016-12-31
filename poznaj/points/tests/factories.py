import factory
from django.contrib.gis import geos


class PointFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'point-{}'.format(n))
    description = 'description'
    geom = geos.fromstr('POINT (0 0)')

    @factory.post_generation
    def images(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for image in extracted:
                self.images.add(image)

    class Meta:
        model = 'points.Point'
