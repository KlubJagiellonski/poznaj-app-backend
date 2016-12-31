from django.db import models

from poznaj.points.models import Point


class Story(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    points = models.ManyToManyField(Point)

    def __str__(self):
        return 'Story: {}'.format(self.title)
