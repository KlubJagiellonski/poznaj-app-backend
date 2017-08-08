from django.test import TransactionTestCase

from poznaj.points.tests.factories import PointFactory
from poznaj.stories.tests.factories import StoryFactory


class TestStoryModelMethods(TransactionTestCase):

    def test_get_all_points(self):
        point = PointFactory()
        story = StoryFactory.create()
        story.points = (point,)
        story.save()
        with self.assertNumQueries(1):
            self.assertQuerysetEqual(story.get_all_points(), ['<Point: {}>'.format(str(point))])
