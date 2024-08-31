from rest_framework.routers import DefaultRouter
from ..genre.views import GenderViewset
from ..statu.views import StatusViewSet

router = DefaultRouter()

router.register(r'status', StatusViewSet, basename='status')
router.register(r'gender', GenderViewset, basename='gender')

urlpatterns = router.urls