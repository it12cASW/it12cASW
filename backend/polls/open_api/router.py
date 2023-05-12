from rest_framework.routers import DefaultRouter
from polls.open_api.views.comment_view import ComentarioViewSet

router = DefaultRouter()
router.register('comentarios', ComentarioViewSet, basename='comentarios')

urlpatterns = router.urls


