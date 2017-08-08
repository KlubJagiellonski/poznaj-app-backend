import factory
from django.contrib.gis import geos


class PointFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'point-{}'.format(n))
    description = 'description'
    geom = geos.fromstr('POINT (0 0)')

    class Meta:
        model = 'points.Point'
