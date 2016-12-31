from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from poznaj.images.views import ImagesViewSet
from poznaj.points.views import PointsViewSet
from poznaj.stories.views import StoriesViewSet

router = routers.DefaultRouter()
router.register(r'images', ImagesViewSet)
router.register(r'points', PointsViewSet)
router.register(r'stories', StoriesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
