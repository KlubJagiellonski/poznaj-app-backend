from django.contrib.gis import admin

from .models import Point

admin.site.register(Point, admin.OSMGeoAdmin)
