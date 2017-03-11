import datetime

import factory

from poznaj.points.tests.factories import PointFactory


class StoryFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'story-{}'.format(n))
    description = 'description'
    duration = factory.LazyFunction(datetime.timedelta)
    first_point = factory.SubFactory(PointFactory)

    @factory.post_generation
    def points(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for point in extracted:
                self.points.add(point)

    class Meta:
        model = 'stories.Story'
