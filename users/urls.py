from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.UserViewSet, basename='user')

urlpatterns = router.urls
