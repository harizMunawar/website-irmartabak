from rest_framework import routers
from backend.viewsets import martabakViewSet

router = routers.DefaultRouter()
router.register(r'martabak', martabakViewSet)