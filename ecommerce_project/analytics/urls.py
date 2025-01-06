from rest_framework.routers import DefaultRouter
from .views import ProductViewViewSet

router = DefaultRouter()
router.register(r'product-views', ProductViewViewSet)

urlpatterns = router.urls
