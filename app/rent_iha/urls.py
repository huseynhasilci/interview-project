from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from rent_iha import views


router = DefaultRouter()
router.register('team', views.TeamViewSet)
router.register('part', views.PartViewSet)
router.register('aircraft', views.AircraftViewSet)

app_name = 'rent_iha'

urlpatterns = [
    path('', include(router.urls)),
]
