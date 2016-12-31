from django.contrib.gis.db import models as gis_models
from django.db import models

from poznaj.images.models import Image


class Point(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    geom = gis_models.PointField()
    images = models.ManyToManyField(Image)

    def __str__(self):
        return 'Point: {}'.format(self.title)
