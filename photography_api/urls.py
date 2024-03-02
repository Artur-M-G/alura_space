from django.urls import path, include
from rest_framework import routers
from .views import PhotographyViewSet

routers = routers.DefaultRouter()
routers.register('Photographys', PhotographyViewSet, basename='Photographys')

urlpatterns = [
    path('', include(routers.urls))
]
