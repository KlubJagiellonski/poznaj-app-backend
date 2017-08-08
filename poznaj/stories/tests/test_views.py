from django.contrib.gis import geos
from django.urls import reverse
from rest_framework import status
from test_plus.test import TestCase

from poznaj.points.tests.factories import PointFactory
from poznaj.stories.filters import WRONG_LAT_LONG_TEXT

from .factories import StoryFactory


class TestStoriesViewSet(TestCase):
    def setUp(self):
        self.point = PointFactory.create()
        self.story = StoryFactory.create()
        self.list_url = reverse('story-list')
        self.detail_url = reverse('story-detail', kwargs={'pk': self.story.id})
        self.user = self.make_user('user_one')
        self.client.login(username=self.user.username, password='password')

    def test_get_all_stories(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), [
                {
                    'id': self.story.id,
                    'title': self.story.title,
                    'description': self.story.description,
                    'duration': '{:02}:00:{:02}'.format(
                        self.story.duration.days, self.story.duration.seconds
                    ),
                    'story_images': []
                }
            ]
        )

    def test_filter_story(self):
        first_point = PointFactory(geom=geos.fromstr('POINT (9 9)'))
        first_story = StoryFactory.create(first_point=first_point)
        first_story.points = (self.point, )
        first_story.save()
        list_url_with_filter = '{}?lat=10.00&long=10.00'.format(reverse('story-list'))
        response = self.client.get(list_url_with_filter, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [first_story.id, self.story.id], [story['id'] for story in response.json()]
        )

    def test_filter_wrong_arguments(self):
        wrong_filter_url = '{}?lat=not_float&long=the_same'.format(reverse('story-list'))
        response = self.client.get(wrong_filter_url, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), [WRONG_LAT_LONG_TEXT])

    def test_get_all_points_for_story(self):
        url = reverse('story-points', kwargs={'pk': self.story.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), [
                {
                    'geometry': {
                        'coordinates': [
                            self.story.first_point.geom.x, self.story.first_point.geom.y
                        ],
                        'type': 'Point'
                    },
                    'properties': {
                        'description': self.story.first_point.description,
                        'point_images': [],
                        'title': self.story.first_point.title
                    },
                    'type': 'Feature'
                },
                {
                    'features': [],
                    'type': 'FeatureCollection'
                }
            ]
        )
