from rest_framework.routers import DefaultRouter
from ..genre.views import GenderViewset
from ..statu.views import StatusViewSet
from ..author.views import AuthorViewset
from ..book.views import  BookViewset

router = DefaultRouter()

router.register(r'status', StatusViewSet, basename='status')
router.register(r'gender', GenderViewset, basename='gender')
router.register(r'author', AuthorViewset, basename='author')
router.register(r'book', BookViewset, basename='book')

urlpatterns = router.urls