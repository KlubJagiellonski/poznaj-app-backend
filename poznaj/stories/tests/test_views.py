import json

from django.contrib.gis import geos
from django.urls import reverse
from rest_framework import status
from test_plus.test import TestCase

from poznaj.points.tests.factories import PointFactory
from poznaj.stories.filters import WRONG_LAT_LONG_TEXT
from poznaj.stories.models import Story

from .factories import StoryFactory


class TestStoriesViewSet(TestCase):
    def setUp(self):
        self.point = PointFactory()
        self.story = StoryFactory.create(points=(self.point,))
        self.list_url = reverse('story-list')
        self.detail_url = reverse('story-detail', kwargs={'pk': self.story.id})
        self.user = self.make_user('user_one')
        self.client.login(username=self.user.username, password='password')

    def test_get_all_stories(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                'id': self.story.id,
                'points': [self.point.id],
                'title': self.story.title,
                'first_point': self.story.first_point.id,
                'description': self.story.description,
                'duration': '{:02}:00:{:02}'.format(
                    self.story.duration.days, self.story.duration.seconds
                )
            }]
        )

    def test_create_story(self):
        response = self.client.post(
            self.list_url,
            data={
                'title': 'my_story',
                'description': 'example_description',
                'duration': '00:01:00',
                'points': [self.point.id],
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 2)
        database_story = Story.objects.get(title='my_story')
        self.assertEqual(database_story.description, 'example_description')
        self.assertEqual(str(database_story.duration), '0:01:00')

    def test_delete_story(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Story.objects.count(), 0)

    def test_update_story(self):
        response = self.client.put(
            self.detail_url,
            data=json.dumps(
                {
                    'title': 'new_title',
                    'description': 'new_description',
                    'duration': '01:00:00',
                    'points': [self.point.id],
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Story.objects.count(), 1)
        database_story = Story.objects.get()
        self.assertEqual(database_story.title, 'new_title')
        self.assertEqual(database_story.description, 'new_description')
        self.assertEqual(str(database_story.duration), '1:00:00')

    def test_filter_story(self):
        first_point = PointFactory(geom=geos.fromstr('POINT (9 9)'))
        first_story = StoryFactory.create(first_point=first_point, points=(self.point,))
        list_url_with_filter = '{}?lat=10.00&long=10.00'.format(
            reverse('story-list')
        )
        response = self.client.get(list_url_with_filter, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [first_story.id, self.story.id],
            [story['id'] for story in response.json()]
        )

    def test_filter_wrong_arguments(self):
        wrong_filter_url = '{}?lat=not_float&long=the_same'.format(
            reverse('story-list')
        )
        response = self.client.get(wrong_filter_url, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            [WRONG_LAT_LONG_TEXT]
        )

    def test_get_all_points_for_story(self):
        url = reverse('story-points', kwargs={'pk': self.story.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'features': [
                    {
                        'properties': {
                            'images': [],
                            'description': self.point.description,
                            'title': self.point.title
                        },
                        'geometry': {
                            'coordinates': [self.point.geom.x, self.point.geom.y], 'type': 'Point'
                        },
                        'type': 'Feature'
                    }
                ],
                'type': 'FeatureCollection'
            }
        )
