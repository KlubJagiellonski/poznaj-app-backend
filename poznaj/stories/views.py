from rest_framework import permissions, viewsets

from .filters import FirstPointFilter
from .models import Story
from .serializers import StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (FirstPointFilter,)
    ordering_fields = ('first_point',)
