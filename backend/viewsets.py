from rest_framework import viewsets, permissions
from .models import martabak
from .serializer import MartabakSerializer

class martabakViewSet(viewsets.ModelViewSet):
    queryset = martabak.objects.all()
    serializer_class = MartabakSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)