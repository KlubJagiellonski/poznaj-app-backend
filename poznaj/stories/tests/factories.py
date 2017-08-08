import datetime

import factory

from poznaj.points.tests.factories import PointFactory


class StoryFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'story-{}'.format(n))
    description = 'description'
    duration = factory.LazyFunction(datetime.timedelta)
    first_point = factory.SubFactory(PointFactory)

    class Meta:
        model = 'stories.Story'
