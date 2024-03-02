from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Photography
from .serializers import PhotographySerializer

class PhotographyViewSet(viewsets.ModelViewSet):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer
    http_method_names = ['get', 'post', 'patch', 'put']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name',]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = self.request.build_absolute_uri() + id
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(cache_page(0))
    def dispatch(self, *args, **kwargs):
        return super(PhotographyViewSet, self).dispatch(*args, **kwargs)
