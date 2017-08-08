from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from poznaj.points.serializers import PointSerializer

from .filters import FirstPointFilter
from .models import Story
from .serializers import StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_backends = (FirstPointFilter,)
    ordering_fields = ('first_point',)

    @detail_route(
        methods=['get'],
        url_path='points'
    )
    def get_all_points_for_story(self, request, pk=None):
        story_obj = self.get_object()
        first_point = story_obj.first_point
        points = story_obj.get_all_points()
        first_point_serializer = PointSerializer(first_point)
        points_serializer = PointSerializer(points, many=True)
        return Response([first_point_serializer.data, points_serializer.data])
