from rest_framework.routers import DefaultRouter
from polls.open_api.views.comment_view import ComentarioViewSet
from polls.open_api.views.user_view import UserViewSet
from polls.open_api.views.issue_view import IssueViewSet

router = DefaultRouter()
router.register('comentarios', ComentarioViewSet, basename='comentarios')
router.register('users', UserViewSet, basename='users')
router.register('issues', IssueViewSet, basename='issues')
urlpatterns = router.urls