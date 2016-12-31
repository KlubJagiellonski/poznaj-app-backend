import datetime

import factory


class StoryFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'point-{}'.format(n))
    description = 'description'
    duration = factory.LazyFunction(datetime.timedelta)

    @factory.post_generation
    def points(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for point in extracted:
                self.points.add(point)

    class Meta:
        model = 'stories.Story'
