from django.conf.urls import url

from .views import TeamView, PartnersView

urlpatterns = [
    url(r'^team/$', TeamView.as_view()),
    url(r'^partners/$', PartnersView.as_view()),
]
