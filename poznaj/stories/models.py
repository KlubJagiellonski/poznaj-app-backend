from django.contrib.gis.db import models as gis_models
from django.db import models

from poznaj.points.models import Point


class Story(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    first_point = models.ForeignKey(Point, related_name='first_point', null=True)
    points = models.ManyToManyField(Point)

    objects = gis_models.GeoManager()

    def __str__(self):
        return 'Story: {}'.format(self.title)
