import json

from django.urls import reverse
from rest_framework import status
from test_plus.test import TestCase

from poznaj.points.tests.factories import PointFactory
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
                'points': [
                    'http://testserver{}'.format(
                        reverse('point-detail', kwargs={'pk': self.point.id})
                    )
                ],
                'title': self.story.title,
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
                'duration': '00:01:00'
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
                    'points': [
                        'http://testserver{}'.format(
                            reverse('point-detail', kwargs={'pk': self.point.id})
                        )
                    ],
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
