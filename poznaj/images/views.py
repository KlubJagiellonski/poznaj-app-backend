from rest_framework import permissions, viewsets

from .models import Image
from .serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
