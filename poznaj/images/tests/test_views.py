from django.urls import reverse
from rest_framework import status
from test_plus.test import TestCase

from .factories import ImageFactory


class TestImagesViewSet(TestCase):
    def setUp(self):
        self.image = ImageFactory()
        self.list_url = reverse('image-list')
        self.detail_url = reverse('image-detail', kwargs={'pk': self.image.id})
        self.user = self.make_user('user_one')
        self.client.login(username=self.user.username, password='password')

    def tearDown(self):
        self.image.image_file.delete()

    def test_get_all_images(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), [
                {
                    'copyright': 'CC0',
                    'title': self.image.title,
                    'image_file': 'http://testserver/media/{}'.format(self.image.image_file.name),
                }
            ]
        )
