from rest_framework_gis import serializers

from poznaj.images.serializers import ImageSerializer

from .models import Point


class PointSerializer(serializers.GeoFeatureModelSerializer):
    point_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Point
        geo_field = 'geom'
        fields = ('title', 'description', 'geom', 'point_images')
