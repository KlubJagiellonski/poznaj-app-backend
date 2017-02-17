from rest_framework_gis import serializers

from .models import Point


class PointSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Point
        geo_field = 'geom'
        fields = ('title', 'description', 'geom', 'images')
