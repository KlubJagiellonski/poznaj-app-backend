from rest_framework import permissions, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from poznaj.points.serializers import PointSerializer

from .filters import FirstPointFilter
from .models import Story
from .serializers import StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (FirstPointFilter,)
    ordering_fields = ('first_point',)

    @detail_route(
        methods=['get'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly],
        url_path='points'
    )
    def get_all_points_for_story(self, request, pk=None):
        instance = self.get_object().get_all_points()
        serializer = PointSerializer(instance, many=True)
        return Response(serializer.data)
