from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.splash.api.serializers import SplashEventSerializer
from apps.splash.filters import SplashEventFilter
from apps.splash.models import SplashEvent


class SplashEventViewSet(ReadOnlyModelViewSet):
    queryset = SplashEvent.objects.all()
    serializer_class = SplashEventSerializer
    page_size = 30
    filter_class = SplashEventFilter
    filter_fields = ('start_time', 'end_time')
    ordering_fields = ('id', 'start_time', 'end_time')