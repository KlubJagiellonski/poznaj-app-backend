from rest_framework import serializers

from poznaj.points.models import Point

from .models import Story


class StorySerializer(serializers.ModelSerializer):
    points = serializers.HyperlinkedRelatedField(
        queryset=Point.objects.all(),
        view_name='point-detail',
        many=True
    )

    class Meta:
        model = Story
        fields = '__all__'
