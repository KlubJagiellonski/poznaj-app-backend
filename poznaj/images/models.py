from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(blank=True)
    copyright = models.CharField(max_length=200, blank=True)
    story = models.ForeignKey(
        'stories.Story',
        related_name='story_images',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_constraint=False
    )
    point = models.ForeignKey(
        'points.Point',
        related_name='point_images',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_constraint=False
    )

    def __str__(self):
        return 'Image: {}'.format(self.title)
