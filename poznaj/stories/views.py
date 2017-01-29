from rest_framework import permissions, viewsets

from .models import Story
from .serializers import StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
