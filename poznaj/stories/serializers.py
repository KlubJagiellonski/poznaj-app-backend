from rest_framework import serializers

from poznaj.images.serializers import ImageSerializer

from .models import Story


class StorySerializer(serializers.HyperlinkedModelSerializer):
    story_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ('id', 'title', 'description', 'duration', 'story_images')
