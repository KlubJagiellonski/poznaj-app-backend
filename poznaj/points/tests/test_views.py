from django.urls import reverse
from rest_framework import status
from test_plus.test import TestCase

from poznaj.images.tests.factories import ImageFactory

from .factories import PointFactory


class TestPointsViewSet(TestCase):
    def setUp(self):
        self.point = PointFactory.create()
        self.image = ImageFactory.create(point=self.point, story=None)
        self.second_point = self.image.point
        self.list_url = reverse('point-list')
        self.detail_url = reverse('point-detail', kwargs={'pk': self.point.id})
        self.user = self.make_user('user_one')
        self.client.login(username=self.user.username, password='password')

    def tearDown(self):
        self.image.image_file.delete()

    def test_get_all_points(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [self.point.geom.x, self.point.geom.y]
                        },
                        'properties': {
                            'title': self.point.title,
                            'description': self.point.description,
                            'point_images': [{
                                'copyright': self.image.copyright,
                                'image_file': 'http://testserver/media/{}'.format(
                                    self.image.image_file.name
                                ),
                                'title': self.image.title
                            }],
                        }
                    }
                ]
            }
        )
