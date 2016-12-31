from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from poznaj.images.tests.factories import ImageFactory
from poznaj.points.models import Point

from .factories import PointFactory


class TestPointsViewSet(APITestCase):

    def setUp(self):
        self.image = ImageFactory()
        self.point = PointFactory.create(images=(self.image,))
        self.list_url = reverse('point-list')
        self.detail_url = reverse('point-detail', kwargs={'pk': self.point.id})

    def test_get_all_points(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
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
                            'images': [
                                'http://testserver{}'.format(
                                    reverse('image-detail', kwargs={'pk': self.image.id})
                                )
                            ],
                        }
                    }
                ]
            }
        )

    def test_create_point(self):
        response = self.client.post(
            self.list_url,
            data={'title': 'example_point', 'description': 'example_desc', 'geom': 'POINT (1 1)'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Point.objects.count(), 2)
        database_point = Point.objects.get(title='example_point')
        self.assertEqual(database_point.description, 'example_desc')
        self.assertEqual(database_point.geom.wkt, 'POINT (1 1)')

    def test_delete_point(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Point.objects.count(), 0)

    def test_update_point(self):
        response = self.client.put(
            self.detail_url,
            data={'title': 'new_title', 'description': 'new_description', 'geom': 'POINT (2 2)'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Point.objects.count(), 1)
        database_point = Point.objects.get()
        self.assertEqual(database_point.title, 'new_title')
        self.assertEqual(database_point.description, 'new_description')
        self.assertEqual(database_point.geom.wkt, 'POINT (2 2)')
