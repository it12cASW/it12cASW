from rest_framework.routers import DefaultRouter
from polls.open_api.views.comment_view import ComentarioViewSet
from polls.open_api.views.user_view import UserViewSet

router = DefaultRouter()
router.register('comentarios', ComentarioViewSet, basename='comentarios')
router.register('users', UserViewSet, basename='users')
# router.register('users/login', UserViewSet, basename='users/login')
# router.register('users/register', UserViewSet, basename='users/register')

urlpatterns = router.urls


