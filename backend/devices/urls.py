from rest_framework.routers import DefaultRouter
from .views import MikrotikDeviceViewSet

router = DefaultRouter()
router.register(r'devices', MikrotikDeviceViewSet, basename="devices")

urlpatterns = router.urls
